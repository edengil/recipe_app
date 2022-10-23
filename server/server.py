from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi import FastAPI, Request, Response
import uvicorn
import requests
from server_functions import *
import re
from fastapi.responses import FileResponse
from fastapi import FastAPI, Request
import uvicorn
import requests

from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()


# app.mount("/", StaticFiles(directory="server\client",
#           html=True), name="client")


# @app.get("/")
# async def get_client():
#     return FileResponse('server\\client\index.html')


@app.get("/sanity")
async def server_is_set_up():
    return {"Message": "OK"}


@app.get("/recipes")
async def get_recipes(ingredient, fillterGluten=False, fillterDairy=False):
    all_recipes = get_recipes_by_ingredient(ingredient)
    all_recipes = all_recipes
    for recipe in all_recipes:
        recipe["hasGluten"] = str(hasGluten(recipe))
        recipe["hasDairy"] = str(hasDairy(recipe))

    
    fillterGluten = False if fillterGluten == "False" or "false" else True
    fillterDairy = False if fillterDairy == "False" or "false" else True

    if fillterGluten:
        all_recipes = [
            recipe for recipe in all_recipes if not hasGluten(recipe)]
    if fillterDairy:
        all_recipes = [
            recipe for recipe in all_recipes if not hasDairy(recipe)]
    return all_recipes


app.mount("/", StaticFiles(directory="server\client",
          html=True), name="client")

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
