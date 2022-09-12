city_data = open('CityProfitsWithMetaData.txt', 'r')
city_name = city_data.readline().rstrip('\n')
while city_name != '':
    num_counties = int(city_data.readline())
    total = 0
    for i in range(num_counties):
        total += float(city_data.readline())

    print(city_name, "Total for State is $", total)
    city_name = city_data.readline().rstrip('\n')
city_data.close()