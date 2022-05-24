from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/jenny")
async def hi_jenny():
    return {"message": "Jenny is very very smart and very beautiful and too good for the husky dog."}
