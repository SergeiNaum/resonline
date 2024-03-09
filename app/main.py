from fastapi import FastAPI, Body
from fastapi.responses import FileResponse

from chemas import SNums

some_file_path = "index.html"
app = FastAPI()


@app.get("/")
async def root():
    return FileResponse(some_file_path)



@app.post("/calculate")
async def calculate(body: SNums):
    res = body.num1 + body.num2
    return {'result': res}


# @app.post('/calculate')
# async def calculate(num1: int, num2: int):
#     return {f'sum of numbers {num1} and {num2} is ': f'{num1+num2}'}