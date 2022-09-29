from api import API

class NbaAPI(API):
    def __init__(self, team_name, year):
        self.url = f"http://data.nba.net/10s/prod/v1/{year}/players.json"
        super().__init__(self.url)
        
    
        