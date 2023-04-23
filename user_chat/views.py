import json
import uuid
import redis
import time

# Create your views here.
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync


# python list append is thread safe method
user_list = []
r = redis.Redis(host="127.0.0.1", port=6379)

'''
chat_user: 获取用户列表
chat_msg: 群发信息
'''


# Create your views here.
class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.username = None
        await self.accept()
    
    async def receive(self, text_data):
        print("websocket receive:", text_data)
        data = json.loads(text_data)

        func = data.get('type')
        if hasattr(self, func):
            print("call func:", func)
            await getattr(self, func)(data)
        else:
            print("ignore func:", func)

        # if data.get('type') == "login":
        #     self.send({
        #         "msg": "login success"
        #     })
        # else:
        #     d = {
        #         'type': 'chat_text',
        #         'msg': [data],
        #     }

        #     await self.channel_layer.group_send(
        #         self.room_group_name,
        #         d
        #     )
    async def disconnect(self, close_code):
        print("=====disconnect====")
        if self.username is not None:
            await self.leave_lobby()

    async def join_lobby(self, data=None):
        print("join lobby:", data)
        #self.room_group_name = self.scope['url_route']['kwargs']['room_name'] 
        self.room_group_name = 'chat_lobby' 

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        ua = ''
        headers = self.scope.get('headers', [])
        for key, value in headers:
            if key == b'user-agent':
                ua = str(value)
                break
        client = ':'.join([str(x) for x in self.scope['client']])
        
        # self.username = str(uuid.uuid4())
        self.username = data.get('user')
        r.hset("userList", self.username, json.dumps({
            'username': self.username, 
            'ua': ua, 
            'client': client,
            'login_time': int(time.time())
            })
        )
        await self.broadcast_user()

    async def leave_lobby(self):
        r.hdel('userList', self.username)
        await self.broadcast_user()

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def broadcast_user(self):
        '''
        获取lobby用户列表
        '''
        print("broadcast user")
        user_list = []
        cur_time = int(time.time())
        for key in r.hkeys('userList'):
            value = r.hget('userList', key)
            value = json.loads(value)
            if cur_time - value['login_time']  > 5 * 60:
                continue
            user_list.append(value)

        data = {
            'type': 'chat_user',
            'msg': user_list,
        }
        await self.channel_layer.group_send(
            self.room_group_name,
            data
        )

    async def chat_user(self, event):
        await self.send(json.dumps(event))

    def chat_msg(self, msg):
        pass

    def chat_text(self, event):
        print("chat_text: ", event)
        msg = event['msg']
        self.send(msg)



    # async def close(self, code=None):
    #     print("=====close====")
    #     await self.channel_layer.group_discard(
    #         self.room_group_name,
    #         self.channel_name
    #     )
    #     r.hdel('userList', self.username)
    #     self.update_user()
    #     return await super().close(code)

GameUserListRedisKey = 'GameUserList'

class GameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        #self.room_name = self.scope['url_route']['kwargs']['room_name'] 
        self.room_name = 'default'
        self.room_group_name = 'game_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        ua = ''
        headers = self.scope.get('headers', [])
        for key, value in headers:
            if key == b'user-agent':
                ua = str(value)
                break
        client = ':'.join([str(x) for x in self.scope['client']])
        
        self.username = str(uuid.uuid4())
        r.hset(GameUserListRedisKey, self.username, json.dumps({
            'username': self.username, 
            'ua': ua, 
            'client': client,
            'login_time': int(time.time())
            })
        )

        await self.update_user()

    async def chat_login(self, event):
        await self.send(json.dumps(event))
    
    async def update_user(self):
        user_list = []
        cur_time = int(time.time())
        for key in r.hkeys(GameUserListRedisKey):
            value = r.hget(GameUserListRedisKey, key)
            value = json.loads(value)
            if cur_time - value['login_time']  > 5 * 60:
                continue
            user_list.append(value)

        d = {
            'type': 'chat_login',
            'msg': user_list,
        }
        await self.channel_layer.group_send(
            self.room_group_name,
            d
        )

    async def receive(self, text_data):
        print("websocket receive:", text_data)
        data = json.loads(text_data)

        d = {
            'type': 'chat_text',
            'msg': [data],
        }
        # self.send(json.dumps(d))
        await self.channel_layer.group_send(
            self.room_group_name,
            d
        )

    async def chat_text(self, event):
        print("chat_text: ", event)
        msg = event['msg']
        self.send(msg)

    async def disconnect(self, close_code):
        print("=====disconnect====")

        r.hdel(GameUserListRedisKey, self.username)
        await self.update_user()

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )