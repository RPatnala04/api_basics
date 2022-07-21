import json
import requests
from single import Single


location = Single("London")
print(location)

print(location.response_data().coord)
print(location.response_data().main)

