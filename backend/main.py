import uvicorn
from fastapi import FastAPI, WebSocket,WebSocketDisconnect
from starlette.middleware.cors import CORSMiddleware
from ConnectionManager import manager
from api.api import api_router

# 配置跨域
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

# 设置路由
app.include_router(api_router)

# 使用websocket实现事时通信
@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)


if __name__ == '__main__':
    uvicorn.run(app='main:app', host="127.0.0.1", port=8000, reload=True, debug=True)
    # uvicorn.run(app='main:app', host="127.0.0.1", port=8000, reload=True, debug=True)
    # uvicorn main:app --reload