from fastapi import FastAPI, Response, status
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

from nba_api import NbaAPI

app = FastAPI()

dream_team = {}

class Player(BaseModel):
    id:str 
    fname:str
    lname:str
    jersey:str
    position:str
    img:str
    dreamTeam:bool


@app.get('/sanity')
def root():
    return {"message":"Server is up and running"}


@app.get('/search')     # ex - localhost:8000/search?teamName=warriors&year=2018&isActive=true
def get_players(response: Response, teamName="warriors", year="2018", active="false"):
    response.headers['Access-Control-Allow-Origin'] = "*"
    data = NbaAPI(teamName, year, active).get_data()
    
    print("server running")
    return data


@app.post('/dreamTeam')
def add_to_dream_team(data: Player, response: Response):
    global dream_team
    dream_team[data.id] = data
    response.status_code = status.HTTP_201_CREATED
    return data


@app.get('/dreamTeam')
def get_dream_team():
    global dream_team
    return list(dream_team.values())


@app.delete('/dreamTeam/{id}')
def remove_from_dream_team(id, response: Response):
    global dream_team
    dream_team.pop(id)
    response.status_code = status.HTTP_204_NO_CONTENT
    
    

app.mount("/", StaticFiles(directory="../Client",html=True), name="Client")


if __name__ == "__main__":
    uvicorn.run("nba-server:app", host="127.0.0.1", port=8000, reload=True)