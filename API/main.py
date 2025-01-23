from fastapi import FastAPI

app = FastAPI()

@app.get("/greet")
def greet_user(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/math")
def add_numbers(a: int, b: int):
    result = a + b
    return {"result": result}
