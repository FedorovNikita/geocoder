import csv

def write_csv(data):
    with open('allData.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((data['url'],
                        data['address'],
                        data['coordinate'],
                        data['count_rooms'],
                        data['price'],
                        data['square'],
                        data['floor'],
                        data['floor_in_building'],
                        data['year_building'],
                        data['child_yard'],
                        data['emergency_house'],
                        data['more_info'],
                        data['number_apartments'],
                        data['energy_class'],
                        data['number_elevators'],
                        data['number_entrances'],
                        data['elevators'],
                        data['number_apartments_without_people'],
                        data['square_number_apartments'],
                        data['square_number_apartments_without_people'],
                        data['square_common_property'],
                        data['land_square_common_property'],
                        data['square_parking'],
                        data['series_type_construction'],
                        data['sports_ground'],
                        data['formation_capital_repair'],
                        data['type_building'],
                        data['equipment'],
                        data['number_chutes'],
                        data['bearing_wall'],
                        data['square_basement'],
                        data['roof'],
                        data['refuse_chute'],
                        data['overlapping'],
                        data['facade'],
                        data['foundation'],
                        data['number_inputs'],
                        data['volume_cesspools'],
                        data['ventilation'],
                        data['water_disposal'],
                        data['drainage_system'],
                        data['gas_supply'],
                        data['hot_water_supply'],
                        data['extinguishing_system'],
                        data['heat_supply'],
                        data['cold_water_supply'],
                        data['electrosupply']))

def main():
    with open("all.csv", "r", newline="", encoding='Windows-1251') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            url = row[0]
            address = row[1]
            coordinate = row[2]
            count_rooms = row[3]
            price = row[4]
            square = row[5]
            floor = row[6]
            floor_in_building = row[7]
            district = row[8]
            # row[9] это дубль row[2]
            year_building = row[10]
            child_yard = row[11]
            emergency_house = row[12]
            more_info = row[13]
            number_apartments = row[14]
            energy_class = row[15]
            number_elevators = row[16]
            number_entrances = row[17]
            elevators = row[18]
            # max_floor = row[19] дубль row[7]
            # min_floor = row[20]
            number_apartments_without_people = row[21]
            square_number_apartments = row[22]
            square_number_apartments_without_people = row[23]
            square_common_property = row[24]
            land_square_common_property = row[25]
            square_parking = row[26]
            series_type_construction = row[27]
            sports_ground = row[28]
            formation_capital_repair = row[29]
            type_building = row[30]
            equipment = row[31]
            number_chutes = row[32]
            bearing_wall = row[33]
            square_basement = row[34]
            roof = row[35]
            refuse_chute = row[36]
            overlapping = row[37]
            facade = row[38]
            foundation = row[39]
            number_inputs = row[40]
            volume_cesspools = row[41]
            ventilation = row[42]
            water_disposal = row[43]
            drainage_system = row[44]
            gas_supply = row[45]
            hot_water_supply = row[46]
            extinguishing_system = row[47]
            heat_supply = row[48]
            cold_water_supply = row[49]
            electrosupply = row[50]

            data = {'url': url,
                'address': address,
                'coordinate': coordinate,
                'count_rooms': count_rooms,
                'price': price,
                'square': square,
                'floor': floor,
                'floor_in_building': floor_in_building,
                'district': district,
                'year_building': year_building,
                'child_yard': child_yard,
                'emergency_house': emergency_house,
                'more_info': more_info,
                'number_apartments': number_apartments,
                'energy_class': energy_class,
                'number_elevators': number_elevators,
                'number_entrances': number_entrances,
                'elevators': elevators,
                'number_apartments_without_people': number_apartments_without_people,
                'square_number_apartments': square_number_apartments,
                'square_number_apartments_without_people': square_number_apartments_without_people,
                'square_common_property': square_common_property,
                'land_square_common_property': land_square_common_property,
                'square_parking': square_parking,
                'series_type_construction': series_type_construction,
                'sports_ground': sports_ground,
                'formation_capital_repair': formation_capital_repair,
                'type_building': type_building,
                'equipment': equipment,
                'number_chutes': number_chutes,
                'bearing_wall': bearing_wall,
                'square_basement': square_basement,
                'roof': roof,
                'refuse_chute': refuse_chute,
                'overlapping': overlapping,
                'facade': facade,
                'foundation': foundation,
                'number_inputs': number_inputs,
                'volume_cesspools': volume_cesspools,
                'ventilation': ventilation,
                'water_disposal': water_disposal,
                'drainage_system': drainage_system,
                'gas_supply': gas_supply,
                'hot_water_supply': hot_water_supply,
                'extinguishing_system': extinguishing_system,
                'heat_supply': heat_supply,
                'cold_water_supply': cold_water_supply,
                'electrosupply': electrosupply}

            write_csv(data)

if __name__ == '__main__':
    main()
