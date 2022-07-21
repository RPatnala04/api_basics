import json
import requests
from single import Single


user_location= input("Enter the location: ")
location = Single(user_location)

print(location.response_data().name)
#print(location.response_data().description)
print(location.response_data().temps)

print(location.response_data().humidity)
print(location.response_data().wind_speed)

print(location.response_data().coord)



print(location.response_data().main)
print(location.response_data().temps_max)
print(location.response_data().temps_min)
#print(location.response_data())

