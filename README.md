# Forecast-API

Forecast-API is a a weather web service, allowing you to get forecaste information. 

Given longitude and latitude, the API return the temperature and precipitation measures in this area. 



## Getting Started
First, clone the repository:
'https://github.com/shiraz-it/Forecast-API.git'

Install project's python dependencies:
'pip install -r requirements.txt'

Create your oun DB using [this](https://github.com/shiraz-it/Forecast-API/blob/master/DBCreation.py) script.

Run [the app](https://github.com/shiraz-it/Forecast-API/blob/master/forecast_api_app.py).

Unless you are using remote web server, the app is running and listening in http://127.0.0.1:5000/. 



## Examples
- For the forecast information in longitude = -180.0 and latitude = -90.0:

http://127.0.0.1:5000/weather/data?lat=-90.0&lon=-180.0

- For the summary of forecast information in longitude = -152.0 and latitude = -90.0, hence the minimu,. maximum and average temperature and precipitation:

http://127.0.0.1:5000/weather/summarize?lat=-90.0&lon=-152.0

Enjoy :) 
