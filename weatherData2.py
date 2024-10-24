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

# # Getting user input for the city name
# city = input("Enter the city name: ")

# # Passing the city name to the URL to get weather data
# url = 'https://wttr.in/{city}'
# res = requests.get(url)

# # Printing the schematic weather details of the city
# print(res.text)

import requests
import sys

# Check if the user has provided a city name as an argument
if len(sys.argv) < 2:
    print("Usage: python weatherData2.py <city_name>")
    sys.exit()

# Get the city name from command-line arguments
city = ' '.join(sys.argv[1:])  # Handles city names with spaces, e.g., "hong kong"

# Pass the city name to the URL to get weather data
url = 'https://wttr.in/{}'.format(city) #.format() is formatting the url with the city name
res = requests.get(url)

# Print the schematic weather details of the city
print(res.text)

#sys is a module to access command line arguments
#sys.argv is a list in Python, which contains the command-line arguments passed to the script.