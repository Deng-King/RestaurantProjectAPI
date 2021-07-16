from fastapi import WebSocket
from typing import List
from dao.user import user_showone


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    # 连接
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    # 断开连接
    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    # 管理员发布公告使用的广播
    async def broadcast_post_notice(self, user_id: int):
        for connection in self.active_connections:
            url = str(connection.url)
            client_id = int(url.split('/')[-1])
            if client_id == user_id:
                continue
            await connection.send_text("1")

    # 服务员提交订单使用的广播
    async def broadcast_post_order(self):
        for connection in self.active_connections:
            url = str(connection.url)
            client_id = int(url.split('/')[-1])
            print(user_showone.show(client_id)[0][3])
            if user_showone.show(client_id)[0][3] == 3:
                await connection.send_text("2")

    # 厨师更改菜品状态使用的广播
    async def broadcast_meal_states(self):
        for connection in self.active_connections:
            url = str(connection.url)
            client_id = int(url.split('/')[-1])
            print(user_showone.show(client_id)[0][3])
            if user_showone.show(client_id)[0][3] == 2:
                await connection.send_text("2")

    # 服务员更改订单状态使用的广播
    async def broadcast_order_states(self):
        for connection in self.active_connections:
            url = str(connection.url)
            client_id = int(url.split('/')[-1])
            print(user_showone.show(client_id)[0][3])
            if user_showone.show(client_id)[0][3] == 1:
                await connection.send_text("2")


manager = ConnectionManager()
