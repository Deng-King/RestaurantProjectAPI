from fastapi import WebSocket
from typing import List
from dao.user import user_showone


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, user_id: int, message: str):
        print(self.active_connections)
        for connection in self.active_connections:
            url = str(connection.url)
            id = int(url.split('/')[-1])
            if user_showone.show(id)[0][3] == user_id:
                continue
            await connection.send_text(message)


manager = ConnectionManager()
