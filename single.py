from single_model import SingleModel
import requests

class Single():

    def __init__(self, cityname):
        self.url= "http://api.openweathermap.org/data/2.5/" \
                  "weather?appid=73041764461c75168f67f580c696f3a4&q="+cityname+ "&units=metric" #own API key

        self.request = requests.get(self.url) #request will contain all the response codes
        self.resp_json = self.request.json() #uses the request # should contain a dictionary

    def response_data(self):
        '''
        Utilised the data model to create the object
        :return: returns the corresponding values from json format
        '''
        return SingleModel(self.resp_json) # utilise the data model to create the object

