# weatherData

This is a simple weather data analysis using Python. 
Simply by asking the user to enter a city name, the program will return the current weather data of the city.

##First Method

We enter the city name in the URL:
"https://www.google.com/search?q="+"weather"+{cityname}

Then we use the `requests` library to get the HTML content of the URL.

We use the `BeautifulSoup` library to parse the HTML content and extract the weather data.

Finally, we print the weather data.

##Second Method

We ask the user to enter the city name.

We enter the city name in the URL: 
https://wttr.in/{city}

Then we use the wttr.in API to get the weather data of the city.

Lastly, we print the weather data.



