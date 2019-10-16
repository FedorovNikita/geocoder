import csv

def write_csv(data):
    with open('address.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((data['address'], data['coord']))

def main():
    with open("cmc2.csv", "r", newline="", encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            address = row[2]
            coord = row[3]
            data = {'address': address, 'coord': coord}
            write_csv(data)

if __name__ == '__main__':
    main()