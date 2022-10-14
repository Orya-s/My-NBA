from fastapi import FastAPI, Response
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from nba_api import NbaAPI

app = FastAPI()


@app.get('/sanity')
def root():
    return {"message":"Server is up and running"}


@app.get('/search')     # ex - localhost:8000/search?teamName=warriors&year=2018&isActive=true
def get_players(response: Response, teamName="warriors", year="2018", active=""):
    response.headers['Access-Control-Allow-Origin'] = "*"
    data = NbaAPI(teamName, year, active).get_data()
    
    print("server running")
    return data


app.mount("/", StaticFiles(directory="../Client",html=True), name="Client")


if __name__ == "__main__":
    uvicorn.run("nba-server:app", host="127.0.0.1", port=8000, reload=True)