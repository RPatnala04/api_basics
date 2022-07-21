from single_model import SingleModel
import requests

class Single():

    def __init__(self, cityname):
        self.url= "http://api.openweathermap.org/data/2.5/" \
                  "weather?appid=73041764461c75168f67f580c696f3a4&q="+cityname

        self.request = requests.get(self.url)
        self.resp_json = self.request.json()

    def response_data(self):
        return SingleModel(self.resp_json)

