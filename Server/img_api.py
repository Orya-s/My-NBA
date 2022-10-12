from api import API


class ImgAPI(API):
    def __init__(self, lname, fname):
        self.url = f"https://nba-players.herokuapp.com/players/{lname}/{fname}"
        super().__init__(self.url)
        self.lname = lname
        self.fname = fname
        self.headers={"Content-Type": "image/png"}
        
    
    def proccess_data(self):
        return self.url
