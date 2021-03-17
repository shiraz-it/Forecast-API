import sqlite3
import pandas as pd

FILE_DIR = 'resources/'
FILE_NAMES = ['file1.csv', 'file2.csv', 'file3.csv']
COLUMNS_TYPES = {'Longitude': float, 'Latitude': float, 'forecastTime': str,
                 'Temperature': float, 'Precipitation': float}


def creating_db():
    conn = sqlite3.connect('climacell_weather_items.db')
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS weather_items")
    cursor.execute("CREATE TABLE weather_items (Longitude float, Latitude float, forecastTime text, "
                   "Temperature float, Precipitation float);")

    for file_name in FILE_NAMES:
        df = pd.read_csv(FILE_DIR+file_name, dtype=COLUMNS_TYPES)
        df.columns = COLUMNS_TYPES.keys()
        if file_name == 'file3.csv':
            df['Precipitation'] = (df['Precipitation'] * 25.4).round(1)
        df.to_sql('weather_items', conn, if_exists='append', index=False)

    conn.close()


creating_db()
