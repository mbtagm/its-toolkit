
import requests

def get_data():
    response = requests.get('https://ec.europa.eu/eurostat/databrowser-backend/api/extraction/1.0/LIVE/false/sdmx/csv/avia_paoc__custom_9948365?startPeriod=1993-01&endPeriod=2023-12&i&compressed=true')