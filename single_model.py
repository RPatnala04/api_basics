''' Data transfer object'''

class SingleModel:

    def __init__(self, single_location): # constructor
        self.main = single_location['main']
        self.coord = single_location['coord']

