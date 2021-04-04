#!/usr/bin/env python -u

from flask import Flask, jsonify, abort, g, request
from utilites import get_valid_request_code, parse_data_res, parse_summ_res, query_db

QUERY_SUMM = """SELECT MIN(Temperature), MIN(Precipitation), MAX(Temperature), MAX(Precipitation), 
                        ROUND(AVG(Temperature), 2), ROUND(AVG(Precipitation), 2) 
                FROM weather_items 
                WHERE Longitude = {lon} AND Latitude = {lat}"""
QUERY_DATA = """SELECT forecastTime, Temperature, Precipitation 
                FROM weather_items 
                WHERE Longitude = {lon} AND Latitude = {lat}"""


app = Flask(__name__)


@app.route('/weather/<handler>', methods=['GET'])
def get_weather_forecast(handler):
    error_code, lat, lon = get_valid_request_code(handler, request)
    if error_code:
        abort(error_code)

    # fitting query string and parsing method according to handler_type
    handler_data = handler == 'data'
    query, parse_result = (QUERY_DATA, parse_data_res) if handler_data else (QUERY_SUMM, parse_summ_res)

    query_result = query_db(query.format(lat=lat,  lon=lon), get_one=not handler_data)

    res_to_display = parse_result(query_result)
    return jsonify(res_to_display)


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


app.run(host= '0.0.0.0')
