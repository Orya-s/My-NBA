import requests



class API:
    def __init__(self, url):
        self.url = url
        self.headers={"Content-Type": "application/json"}


    def call_api(self, attempts = 0):
        try:
            r = requests.get(self.url).json()
            return r
        except Exception as e:
            self.error_handler(self.call_api, attempts, e)       
            
            
    def error_handler(self, method, attempts, error):
        attempts += 1
        if(attempts < 3):
            print(f"Attempt number {attempts}")
            return method(attempts)
        else:
            print("Server error")
            raise error
        
      
    def get_data(self):
        return self.proccess_data(self.call_api())


    def proccess_data(self):
        pass
