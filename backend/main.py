import uvicorn
from fastapi import FastAPI, WebSocket,WebSocketDisconnect
from starlette.middleware.cors import CORSMiddleware
from api.endpoints import cookApi, waiterApi, noticeApi, profilesApi, loginApi, adminApi
from ConnectionManager import manager

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

app.include_router(loginApi.router, prefix="/api")
app.include_router(profilesApi.router, prefix="/api")
app.include_router(noticeApi.router, prefix="/api")
app.include_router(waiterApi.router, prefix="/api")
app.include_router(adminApi.router, prefix="/api")
app.include_router(cookApi.router, prefix="/api")


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast_post_notice(f"Client #{client_id} disconnect")


if __name__ == '__main__':
    uvicorn.run(app='main:app', host="192.168.244.33", port=8000, reload=True, debug=True)
    # uvicorn.run(app='main:app', host="127.0.0.1", port=8000, reload=True, debug=True)
    # uvicorn main:app --reload