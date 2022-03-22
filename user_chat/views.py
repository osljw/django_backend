from django.shortcuts import render

# Create your views here.
from channels.generic.websocket import WebsocketConsumer
import json
import time

# Create your views here.
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        """
        接收消息
        :param text_data: 客户端发送的消息
        :return:
        """
        print("websocket receive:", text_data)
        # poetryList = [
        #     "云想衣裳花想容",
        #     "春风拂槛露华浓",
        #     "若非群玉山头见",
        #     "会向瑶台月下逢",
        # ]
        d = {
            'test': 123
        }
        #for i in poetryList:
        time.sleep(0.5)
        self.send(json.dumps(d))
