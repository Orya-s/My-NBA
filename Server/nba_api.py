from api import API
from img_api import ImgAPI

teams_id = {
    "lakers": "1610612747",
    "warriors": "1610612744",
    "heat": "1610612748",
    "suns": "1610612756"
}


class NbaAPI(API):
    def __init__(self, team_name, year, is_active):
        self.url = f"http://data.nba.net/10s/prod/v1/{year}/players.json"
        super().__init__(self.url)
        self.team = teams_id.get(team_name, None)
        self.year = year
        self.is_active = is_active
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
                    "img": ImgAPI(player["lastName"], player["firstName"]).url,
                    "dreamTeam": False
                    }
                    for player in leagues[league] 
                    if (bool(self.is_active != "true") or bool(player["isActive"]) == True) and player["teamId"] == self.team]
            
            for i in range(len(players)):
                players[i]["id"]= self.team + self.year + str(i)
            self.data = players
            return players 
        
        except Exception as e:
            print("Could not proccess data")
            raise e
       