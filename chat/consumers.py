from channels.generic.websocket import AsyncWebsocketConsumer
import json
import time
import asyncio

# REF: https://channels.readthedocs.io/en/stable/topics/consumers.html#asyncwebsocketconsumer
class RTLogConsumer(AsyncWebsocketConsumer):
  	# websocket 연결 시 실행
    async def connect(self):
        self.user_id = self.scope['url_route']['kwargs']['user_id']
        await self.accept()

    # websocket 연결 종료 시 실행 
    async def disconnect(self, close_code):
        pass

    # 클라이언트로부터 메세지를 받을 시 실행
    async def receive(self, text_data):
        print(f'{self.user_id}: start scraping...')

        await asyncio.sleep(3)       # 3 sec work

        await self.send(text_data=json.dumps({
            'message': 'first work finished...'
        }))

        await asyncio.sleep(3)       # 3 sec work

        await self.send(text_data=json.dumps({
            'message': 'second work finished...'
        }))

        await asyncio.sleep(3)       # 3 sec work

        await self.send(text_data=json.dumps({
            'message': 'All work finished!!'
        }))

        print(f'{self.user_id}: end scraping...')