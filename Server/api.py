from distutils.log import warn
import requests



class API:
    def __init__(self, url):
        self.url = url
        self.headers={"Content-Type": "application/json"}


    def call_api(attempts = 0):
        pass
            
            
    def error_handler(method, attempts, error):
        attempts += 1
        if(attempts < 3):
            print(f"Attempt number {attempts}")
            return method(attempts)
        else:
            print("Server error")
            raise error
        
      
    def get_data(self):
        response = requests.get(self.url, self.headers)
        return response.json()


    def proccess_data(self):
        pass
