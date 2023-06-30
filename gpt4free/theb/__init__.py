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

    timer = None
    message_queue = Queue()
    stream_completed = False
    last_msg_id = None

    @staticmethod
    def request(prompt: str, proxy: Optional[str] = None, steam=True):
        headers = {
            'authority': 'chatbot.theb.ai',
            'content-type': 'application/json',
            'origin': 'https://chatbot.theb.ai',
            'user-agent': UserAgent().random,

            # 'accept': 'application/json, text/plain, */*',
            # 'accept-encoding': 'gzip, deflate, br',
            # 'dnt': '1',
            # 'referer': 'https://chatbot.theb.ai/',
        }

        proxies = {'http': 'http://' + proxy, 'https': 'http://' + proxy} if proxy else None
        
        options = {}
        if Completion.last_msg_id:
            options['parentMessageId'] = Completion.last_msg_id

        # print("headers:", headers)
        # print("proxies:", proxies)
        # print("options:", options)
        
        response = requests.post(
            'https://chatbot.theb.ai/api/chat-process',
            headers=headers,
            proxies=proxies,
            content_callback=Completion.handle_stream_response,
            json={'prompt': prompt, 'options': options},
            timeout=5000, # milliseconds
            impersonate='chrome101'
        )

        # print("response:", response)
        # print("response status_code:", response.status_code)
        # # print("response json:", response.json())
        # print("response content:", response.content, response.headers)
        # print("response text:", response.text)

        Completion.stream_completed = True
        return response
    
    @staticmethod
    def create(prompt: str, proxy: Optional[str] = None) -> Generator[str, None, None]:
        Completion.stream_completed = False
        
        while not Completion.message_queue.empty():
            Completion.message_queue.get()

        Thread(target=Completion.request, args=[prompt, proxy]).start()

        content_byte = bytearray()
        while not Completion.stream_completed or not Completion.message_queue.empty():
            try:
                cur = Completion.message_queue.get(timeout=0.01)

                if len(Completion.part2) < len(cur) and cur[-len(Completion.part2):] == Completion.part2.encode('utf-8'):
                    content_byte += cur
                else:
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

    @staticmethod
    def handle_stream_response(response):
        # print("\n\nresponse:", response)
        # print("\n\nresponse type:", type(response), " content:", response)
        # Completion.message_queue.put(response.decode())
        Completion.message_queue.put(response)

    @staticmethod
    def get_response(prompt: str, proxy: Optional[str] = None) -> str:
        response_list = []
        for message in Completion.create(prompt, proxy):
            response_list.append(message)
        return ''.join(response_list)
        
        Completion.message_queue.put(response.decode(errors='replace'))
