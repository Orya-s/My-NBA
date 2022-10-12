from api import API
from img_api import ImgAPI

teams_id = {
    "lakers": "1610612747",
    "warriors": "1610612744",
    "heat": "1610612748",
    "suns": "1610612756"
}


class NbaAPI(API):
    def __init__(self, team_name, year):
        self.url = f"http://data.nba.net/10s/prod/v1/{year}/players.json"
        super().__init__(self.url)
        self.year = year
        self.team = teams_id[team_name]
        self.headers = {"Content-Type": "application/json"}
        
    
    def proccess_data(self, unproccessed_data):
        # recieves api data: filters according to year and returns
        try:
            leagues = unproccessed_data["league"]
            players = []
            for league in leagues:
                players += [
                    {"fname": player["firstName"],
                    "lname":player["lastName"],
                    "jersey":player["jersey"],
                    "position":player["pos"],
                    "img": ImgAPI(player["lastName"], player["firstName"]).url
                    }
                    for player in leagues[league] if bool(player["isActive"]) == True and player["teamId"] == self.team]
            
            for i in range(len(players)):
                players[i]["id"]= f"card{i}"
            self.data = players
            return players 
        
        except Exception as e:
            print("Could not proccess data")
            raise e
       