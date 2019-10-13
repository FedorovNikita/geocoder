import pandas, os
import csv
# from time import sleep
# from random import uniform
import geocoder
import geopy
from geopy.geocoders import Yandex


def write_csv(data):
    with open('cmc3.csv', 'a', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow((data['address'], data['coord']))

def main():
    df1 = pandas.read_csv('cmc.csv', encoding='utf-8')
    nom = Yandex(api_key="e3523b18-24d4-44fd-aaf5-f6a2c2cfb0d0", timeout=5)
    # df1["coordinates"] = df1["Адрес"].apply(nom.geocode)
    df1["coordinates"] = df1["Адрес"][0:10].apply(nom.geocode)

    lenCoord = len(df1["coordinates"]) - 1
    i = 0
    while i < 10: #lenCoord
        lt = df1["coordinates"][i].latitude
        ln = df1["coordinates"][i].longitude
        address = df1["coordinates"][i]
        coord = str(lt) + ', ' + str(ln)
        print(i, address, lt, ln)
        i = i + 1
        data = {'address': address, 'coord': coord}
        write_csv(data) 

if __name__ == '__main__':
    main()
