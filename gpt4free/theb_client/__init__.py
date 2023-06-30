from json import loads
from queue import Queue, Empty
from re import findall
from threading import Thread
from typing import Generator, Optional

from curl_cffi import requests
from fake_useragent import UserAgent


class Completion:
    # experimental
    part1 = '{"role":"assistant","id":"chatcmpl'
    part2 = '"},"index":0,"finish_reason":null}]}}'
    regex = rf'{part1}(.*){part2}'

    def __init__(self) -> None:
        self.timer = None
        self.message_queue = Queue()
        self.stream_completed = False
        self.last_msg_id = None

    def request(self, prompt: str, proxy: Optional[str] = None):
        headers = {
            'authority': 'chatbot.theb.ai',
            'content-type': 'application/json',
            'origin': 'https://chatbot.theb.ai',
            'user-agent': UserAgent().random,
        }

        proxies = {'http': 'http://' + proxy, 'https': 'http://' + proxy} if proxy else None
        
        options = {}
        if self.last_msg_id:
            options['parentMessageId'] = self.last_msg_id
        
        response = requests.post(
            'https://chatbot.theb.ai/api/chat-process',
            headers=headers,
            proxies=proxies,
            content_callback=self.handle_stream_response,
            json={'prompt': prompt, 'options': options},
            timeout=5000, # milliseconds
            impersonate='chrome101'
        )

        self.stream_completed = True
        return response
    

    def create(self, info: dict, proxy: Optional[str] = None) -> Generator[str, None, None]:
        prompt = info['prompt']

        self.stream_completed = False
        
        while not self.message_queue.empty():
            self.message_queue.get()

        Thread(target=self.request, args=[prompt, proxy]).start()

        content_byte = bytearray()
        while not self.stream_completed or not self.message_queue.empty():
            try:
                cur = self.message_queue.get(timeout=0.01)

                if len(Completion.part2) < len(cur) and cur[-len(Completion.part2):] == Completion.part2.encode('utf-8'):
                    # 完整信息
                    content_byte += cur
                else:
                    # 信息不完整，继续接收
                    content_byte += cur
                    continue

                message = content_byte.decode()
                # print("\n\n message:", message)
                for message in findall(Completion.regex, message):
                    # print("=========extract message:", message)
                    message_json = loads(Completion.part1 + message + Completion.part2)
                    Completion.last_msg_id = message_json['id']
                    yield message_json['delta']
                content_byte = bytearray()

            except Empty:
                pass
            except UnicodeDecodeError:
                print("\n\nUnicodeDecodeError:", content_byte)
                print("")

    def handle_stream_response(self, response):
        self.message_queue.put(response)

    # @staticmethod
    # def get_response(prompt: str, proxy: Optional[str] = None) -> str:
    #     response_list = []
    #     for message in Completion.create(prompt, proxy):
    #         response_list.append(message)
    #     return ''.join(response_list)
        
    #     Completion.message_queue.put(response.decode(errors='replace'))
