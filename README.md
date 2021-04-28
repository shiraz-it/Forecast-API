
# Forecast-API

Forecast-API is a a weather web service, allowing you to get forecaste information. 

Given longitude and latitude, the API return the temperature and precipitation measures in this area. 


## Getting Started - AWS EC2 as Server
Originaly this project used AWS- an EC2 instance with python virtual evnironment. 

In this case, instalation works bit different:

1. Open SSH connection with .pem file.

2. Use the package-management system of the server operation system to install requirements. 


Alternatively, if package-management system can't install some requirements (like yum):

1. Install Python 3.6:

> sudo yum install rh-python36
 
2. Create new virtual environment:

> python3 -m venv venv

3. Activate the virtual environment:

> source venv/bin/activate

4. Install git in your EC2 instance, and clone this repository:

> sudo yum install git -y
> git clone https://github.com/shiraz-it/Forecast-API.git 

5. Install project's python dependencies (no need to mention pip3 in venv):

> pip install -r requirements.txt
 
6. Create your oun DB:
> python DBCreation.py

7. Run the app:
>  python forecast_api_app.py &


## Getting Started - Local Server

1. First, clone the repository:

> git clone https://github.com/shiraz-it/Forecast-API.git

2. Install project's python dependencies:

> pip install -r requirements.txt

3. Create your oun DB using [this](https://github.com/shiraz-it/Forecast-API/blob/master/DBCreation.py) script.

4. Run the [app](https://github.com/shiraz-it/Forecast-API/blob/master/forecast_api_app.py)!

Unless you are using remote web server, the app is running and listening in http://127.0.0.1:5000/. 



## Examples
- For the forecast information in longitude = -180.0 and latitude = -90.0:

http://127.0.0.1:5000/weather/data?lat=-90.0&lon=-180.0

- For the summary of forecast information in longitude = -152.0 and latitude = -90.0, hence the minimum, maximum and average of temperature and precipitation:

http://127.0.0.1:5000/weather/summarize?lat=-90.0&lon=-152.0

Enjoy :) 
