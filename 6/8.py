from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Используйте /square и /add"}


@app.get("/square/{number}")
def square(number: int):
    return {"number": number, "square": number ** 2}


@app.get("/add")
def add_numbers(a: int, b: int):
    result = a + b
    return {"operation": "add", "a": a, "b": b, "result": result}


uvicorn.run(app)
