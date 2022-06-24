from fastapi import FastAPI
from fastapi.responses import JSONResponse
import game

app = FastAPI()

@app.post("/new_character/")
def create_item(name: str, profession: str):
  try:
    game.create_character(name, profession)
    return JSONResponse(status_code=201, content="Character created")
  except Exception as e:
    return JSONResponse(status_code=400, content={"Error": str(e)})