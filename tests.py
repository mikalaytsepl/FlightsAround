test_input = [
    {'callsing': 'RYR90JB', 'line': 'Ryanair', 'icao': 'RYR', 'model': 'B738 Boeing 737-8AS', 'departure_name':
        'Palma de Mallorca Airport', 'departure_icao': 'LEPA', 'time_departure': '20:30', 'arrival_name':
         'Wroclaw Copernicus Airport', 'arrival_icao': 'EPWR', 'time_arrival': '23:15'}, {'callsing': 'DLH6NH', 'line':
        'Lufthansa', 'icao': 'DLH', 'model': 'CRJ9 Mitsubishi CRJ-900LR', 'departure_name': 'Munich Airport',
                                                                                          'departure_icao':
                                                                                              'EDDM',
                                                                                          'time_departure': '22:00',
                                                                                          'arrival_name': 'Wroclaw Copernicus Airport',
                                                                                          'arrival_icao': 'EPWR',
                                                                                          'time_arrival':
                                                                                              '23:05'},
    {'callsing': 'BCS5917', 'line': 'DHL (No.1 Best Workplace Sticker)', 'icao': 'DHK',
     'model': 'B752 Boeing 757-236(PCF)',
     'departure_name': 'Katowice International Airport', 'departure_icao': 'EPKT', 'time_departure': '22:20',
     'arrival_name':
         'Leipzig Halle Airport',
     'arrival_icao': 'EDDP', 'time_arrival': '23:29'}, {'callsing': 'LOT6608', 'line': 'LOT', 'icao': 'LOT', 'model':
        'B738 Boeing 737-86N', 'departure_name': 'Malaga Costa Del Sol Airport', 'departure_icao': 'LEMG',
                                                        'time_departure': '19:10',
                                                        'arrival_name': 'Warsaw Chopin Airport', 'arrival_icao': 'EPWA',
                                                        'time_arrival': '22:59'},
    {'callsing': 'LOT2KH', 'line': 'LOT', 'icao':
        'LOT', 'model': 'E75S Embraer E175STD', 'departure_name': 'Warsaw Chopin Airport', 'departure_icao': 'EPWA',
     'time_departure': '22:40',
     'arrival_name': 'Wroclaw Copernicus Airport',
     'arrival_icao': 'EPWR', 'time_arrival': '23:35'}]


def fill_table(input):
    pref = "LOT"
    for flighr in input:
        for item in flighr.values():
            if pref:
                pref = pref.split("|")
                for preference in pref:
                    if preference in item:
                        print(f"{item} here is it")


fill_table(test_input)
