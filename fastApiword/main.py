from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from tortoise.contrib.fastapi import register_tortoise
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins="http://127.0.0.1:8081",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
# 数据库绑定
register_tortoise(app,
                  db_url="mysql://root:password@localhost:3306/wordmemory",
                  modules={"models": ['dao.models']},
                  generate_schemas=True,
                  add_exception_handlers=True
                  )


@app.get("/")
async def read_root():
    return {"hello", "world"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
if __name__ == '__main__':
    run('main:app', reload=True)