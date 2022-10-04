from fastapi import FastAPI, Response
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import requests
import os

from nba_api import NbaAPI

app = FastAPI()


# static files      - should be at the top of the file!
# first parameter - sub-path for the route, if we want to reach a file example.txt that is found in
# the static folder, it’s route will be /static/example.txt
# second parameter - the StaticFiles function, we pass it a directory="static" keyword argument to 
# specify the directory of the static files 
# example - localhost:8000/static/view.jpg

# app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/Client", StaticFiles(directory="Client"), name="Client")



@app.get('/')
def root(response: Response):
    response.headers['Access-Control-Allow-Origin'] = "*"
    api = NbaAPI("lakers", 2018)
    print(api.headers)
    return {"message":"Server is up and running"}


@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    path = "C:/Users/Rent/Desktop/NBA/Client/static/favicon.ico"
    return FileResponse(path)
    # return FileResponse(path=file_path, headers={"Content-Disposition": "attachment; filename=" + file_name})


@app.get('/search')
def get_players():
    data = NbaAPI("warriors","2018").get_data()
    return data
    # return {"msg":"Players"}





if __name__ == "__main__":
    uvicorn.run("nba-server:app", host="127.0.0.1", port=8000, reload=True)