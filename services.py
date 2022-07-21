import json
import requests
from single import Single


user_location= input("Enter the location: ")
location = Single(user_location)

print("\n")
print("Current City: "+location.response_data().name)
#print(location.response_data().description)
print("Current temperature in Celsius:")
print(location.response_data().temps)

print("Humidity: ")
print(location.response_data().humidity)

print("Wind Speed: ")
print(location.response_data().wind_speed)

print("\n")
print("Location Coordinates (lon, lat) :")
print(location.response_data().coord)

print("\n")
print("Additional details: ")

print("Max temperature for today in Celsius:")
print(location.response_data().temps_max)
print("Min temperature for today in Celsius:")
print(location.response_data().temps_min)


