"""
app/main.py
FastAPI の仮エントリポイント(最小構成)。
現在、% uvicorn main:app --reload コマンドで起動し、http://127.0.0.1:8000 でresponseが返ってくる状態
将来はルーティングだけを残し、詳細は domain / service / repository へ分離予定。
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
