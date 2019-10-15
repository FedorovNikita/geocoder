import pandas
import csv
import geopy
# from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Nominatim
from time import sleep
from random import uniform
from geopy.extra.rate_limiter import RateLimiter

def get_column_name():
    with open('cmc3.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter='\t')
        col0 = 'Адрес'
        col1 = 'Координаты'

        writer.writerow((col0,
                        col1))

def write_csv(data):
    with open('cmc3.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow((data['address'], data['coordinates']))

def main():
    get_column_name()
    df = pandas.read_csv('cmc.csv', encoding='utf-8')
    nom = Nominatim(user_agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 YaBrowser/19.9.3.314 Yowser/2.5 Safari/537.36")
    
    a = 3
    i = 0
    while a <= 50: #len(df) + 1
        sleep(uniform(1,3))
        geocode = RateLimiter(nom.geocode, min_delay_seconds=1)
        while i < a:
            # df.iat[i,3] i - строки и 3 столбец
            geocoder_result = nom.geocode(df.iat[i,3], timeout=10)
            try:
                
                address = geocoder_result.address
                coordinates = str(geocoder_result.latitude) + ', ' + str(geocoder_result.longitude)
                data = {'address': address, 'coordinates': coordinates}
                write_csv(data) 
            except:
                lat = None
                lon = None
                address = None
                coordinates = str(lat) + ', ' + str(lon)
                data = {'address': address, 'coordinates': coordinates}
                write_csv(data)
            i = i + 1
        a = a + 3

if __name__ == '__main__':
    main()
