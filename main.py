import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from api import loginApi

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

app.include_router(loginApi.loginRouter, prefix="/api")


@app.get("/")
async def homepage_info():
    return {"home": "welcome"}


if __name__ == '__main__':
    uvicorn.run(app='main:app', host="127.0.0.1", port=8000, reload=True, debug=True)
