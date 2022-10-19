from api import API


class StatsAPI(API):
    def __init__(self, lname, fname):
        self.url = f"https://nba-players.herokuapp.com/players-stats/{lname}/{fname}"
        super().__init__(self.url)
        self.lname = lname
        self.fname = fname
        
    
    def proccess_data(self):
        try:
            data = self.call_api()
            return {
                "gamesPlayed": data["games_played"],
                "minutesPerGame": data["minutes_per_game"],
                "pointsPerGame": data["points_per_game"],
                "playerEfficiencyRating": data["player_efficiency_rating"]
            }

        except:
            return {
                "gamesPlayed": "Not found",
                "minutesPerGame": "Not found",
                "pointsPerGame": "Not found",
                "playerEfficiencyRating": "Not found"}
        
