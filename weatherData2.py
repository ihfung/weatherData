#method two to get weather data

# Importing the requests module
import requests

# # Sending request to get the IP location information
# res = requests.get('https://ipinfo.io/')
# data = res.json()  # Receiving the response in JSON format

# # Extracting the location of the city from the response
# citydata = data['city']
# print("Current Location:", citydata)

# # Passing the city name to the URL to get weather data
# url = 'https://wttr.in/{}'.format(citydata)
# res = requests.get(url)

# # Printing the schematic weather details of the city
# print(res.text)

# Getting user input for the city name
city = input("Enter the city name: ")

# Passing the city name to the URL to get weather data
url = 'https://wttr.in/{city}'
res = requests.get(url)

# Printing the schematic weather details of the city
print(res.text)