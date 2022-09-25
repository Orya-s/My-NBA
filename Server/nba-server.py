from fastapi import FastAPI, Response
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import requests


app = FastAPI()


# static files      - should be at the top of the file!
# first parameter - sub-path for the route, if we want to reach a file example.txt that is found in
# the static folder, it’s route will be /static/example.txt
# second parameter - the StaticFiles function, we pass it a directory="static" keyword argument to 
# specify the directory of the static files 
# example - localhost:8000/static/view.jpg

# app.mount("/static", StaticFiles(directory="static"), name="static")



@app.get('/')
def root(response: Response):
    
    return {"message":"Server is up and running"}


# @app.get('/search')
# def get_players():
#     return {"msg":"Players"}



if __name__ == "__main__":
    uvicorn.run("nba-server:app", host="127.0.0.1", port=8000, reload=True)