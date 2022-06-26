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


@app.get("/character/{name}")
def retrieve_character(name: str):
    try:
        return game.retrieve_character(name)
    except Exception as e:
        raise e
        return JSONResponse(status_code=400, content={"Error": str(e)})


@app.get("/character/")
def retrieve_all_characters():
    try:
        return game.retrieve_all_characters()
    except Exception as e:
        return JSONResponse(status_code=400, content={"Error": str(e)})

@app.post("/battle/")
def battle(name1: str, name2: str):
    try:
        return game.battle(name1, name2)
    except Exception as e:
        raise e
        return JSONResponse(status_code=400, content={"Error": str(e)})