from fastapi import APIRouter

app_home = APIRouter()


@app_home.get('/', tags=["Intro"])
async def hello():
    return {"message": "Hello!"}
