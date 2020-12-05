from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
import json

class ChatConsumer(AsyncWebsocketConsumer):
  	# websocket 연결 시 실행
    async def connect(self):
        # chat/routing.py 에 있는
        # path('ws/chat/<str:room>/',consumers.ChatConsumer),
        # 에서 room 을 가져옵니다.
        self.room = self.scope['url_route']['kwargs']['room']
        self.room_group_name = 'chat_%s' % self.room

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

        print(self.scope['headers'][10])
        # 접속 후, 접속자 누구인지 알기 위해서 입장을 알려주기
        username = self.scope['user'].username if self.scope['user'].username else str(self.scope['headers'][10][1])[2:7]+ "익명"

        # 각 방에 뿌리는 정보 (이거를 통해서 chat_message 메소드 호출)
        # type으로 함수를 결정해서 해당 메시지를 보내는 형식
        await self.channel_layer.group_send(
            self.room_group_name, {'type': 'greet', 'message': f'\'{username}\'님이 입장하셨습니다.'}
        )

		# websocket 연결 종료 시 실행 
    async def disconnect(self, close_code):
        # Leave room group

        # 연결 종료시 나갔다고 알려주기
        username = self.scope['user'].username if self.scope['user'].username else str(self.scope['headers'][10][1])[2:7]+ "익명"

        # 각 방에 뿌리는 정보 (이거를 통해서 chat_message 메소드 호출)
        # type으로 함수를 결정해서 해당 메시지를 보내는 형식
        await self.channel_layer.group_send(
            self.room_group_name, {'type': 'greet', 'message': f'\'{username}\'님이 퇴장하셨습니다.'}
        )

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        # {}가 chat_message의 event 매소드이다
        # type으로 함수를 결정해서 해당 메시지를 보내는 형식
        await self.channel_layer.group_send(
            self.room_group_name, {'type': 'chat_message', 'message': message, 'user_name': self.scope['user'].username, }
        )

    # Receive message from room group
    async def chat_message(self, event):
        username = event['user_name'] if event['user_name'] else str(self.scope['headers'][10][1])[2:7]+ "익명"
        message = f"{username} : " + event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

    # 환영 및 나가기
    async def greet(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))