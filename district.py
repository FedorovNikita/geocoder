import pandas
import csv

def write_csv(data):
    with open('district.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow((data['address'], data['district']))

def main():
    df = pandas.read_csv('cmc3.csv', encoding='utf-8', sep="\t")
    a = 0
    while a < len(df):
        address = df['Адрес'][a]
        dsArr = address.split(', ')
        i = 0
        district = 'Неизвестный район'
        while i < len(dsArr):
            if dsArr[i] == 'Калининский район':
                district = dsArr[i]
            if dsArr[i] == 'ЧТЗ':
                district = dsArr[i]
            if dsArr[i] == 'ЧМЗ':
                district = dsArr[i]
            if dsArr[i] == 'Курчатовский район':
                district = dsArr[i]
            if dsArr[i] == 'Ленинский район':
                district = dsArr[i]
            if dsArr[i] == 'Центральный район':
                district = dsArr[i]
            if dsArr[i] == 'Советский район':
                district = dsArr[i]
            if dsArr[i] == 'Красноармейсский район':
                district = dsArr[i]
            i = i + 1
        data = {'address': address, 'district': district}
        write_csv(data)
        a = a + 1

if __name__ == '__main__':
    main()
