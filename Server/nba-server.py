from fastapi import FastAPI, Response
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from nba_api import NbaAPI

app = FastAPI()


@app.get('/sanity')
def root():
    return {"message":"Server is up and running"}


@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    path = "C:/Users/Rent/Desktop/NBA/Client/static/favicon.ico"
    return FileResponse(path)
    # return FileResponse(path=file_path, headers={"Content-Disposition": "attachment; filename=" + file_name})


@app.get('/search')     # ex - localhost:8000/search?teamName=warriors&year=2018
def get_players(response: Response, teamName="warriors", year="2018"):
    response.headers['Access-Control-Allow-Origin'] = "*"
    data = NbaAPI(teamName, year).get_data()
    
    print("server running")
    return data


# example - localhost:8000/static/index.html
app.mount("/", StaticFiles(directory="../Client",html=True), name="Client")


if __name__ == "__main__":
    uvicorn.run("nba-server:app", host="127.0.0.1", port=8000, reload=True)