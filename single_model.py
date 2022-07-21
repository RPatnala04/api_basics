''' Data transfer object'''

class SingleModel:

    def __init__(self, single_location): # constructor
        self.name = single_location['name'] #location name

        self.main = single_location['main']
        self.temps = self.main['temp'] #Current temp
        self.temps_min = self.main['temp_min'] #Min temp for the day
        self.temps_max = self.main['temp_max'] #Max temp for the day
        self.humidity = self.main['humidity'] #Humidity of the day

        self.weather = single_location['weather']
        #self.description = self.weather['description'] #Current Weather description

        self.wind = single_location['wind']
        self.wind_speed = self.wind['speed'] #Wind speed

        self.coord = single_location['coord'] #latitude and longitude of location


