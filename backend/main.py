import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from starlette.middleware.cors import CORSMiddleware
from api import loginApi
from api import profilesApi
from api import noticeApi
from api import waiterApi
from api import adminApi
from api import cookApi
from fastapi.responses import HTMLResponse
from settings import html
from ConnectionManager import manager

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

app.include_router(loginApi.loginRouter, prefix="/api")
app.include_router(profilesApi.profilesRouter, prefix="/api")
app.include_router(noticeApi.noticeRouter)
app.include_router(waiterApi.waiterRouter, prefix="/api")
app.include_router(adminApi.adminRouter, prefix="/api")
app.include_router(cookApi.cookRouter, prefix="/api")


@app.get("/")
async def homepage_info():
    return HTMLResponse(html)


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")


if __name__ == '__main__':
    uvicorn.run(app='main:app', host="192.168.246.250", port=8000, reload=True, debug=True)
    # uvicorn main:app --reload