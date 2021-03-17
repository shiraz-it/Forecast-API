import sqlite3
from flask import g

DB_NAME = 'climacell_weather_items.db'
SUMM_TITLES = ['min', 'max', 'avg']


# returns 0 if the request is valid, hence handler_type in ['summarize', 'data'],
# and lat, lon can be converted into float type.
# else, return matching error HTTP status codes for error responses
def get_valid_request_code(handler_type, request):
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    if lat is None or lon is None or handler_type not in ['summarize', 'data']:
        return 400, lat, lon

    try:
        lat, lon = float(lat), float(lon)
        return 0, lat, lon
    except ValueError:
        return 422, lat, lon


# get the current database connection
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DB_NAME)
    return db


# query function that combines getting the cursor, executing and fetching the results.
# return one row or the whole query result according to get_one flag
def query_db(query, args=(), get_one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if get_one else rv


def parse_data_res(query_result):
    return [dict(forecastTime=row[0], Temperature=row[1], Precipitation=row[2]) for row in query_result]


def parse_summ_res(query_result):
    if query_result[0] is None:
        return []
    zipped_result = zip(SUMM_TITLES, query_result[::2], query_result[1::2])
    return {title: dict(Temperature=temp, Precipitation=prec) for title, temp, prec in zipped_result}

