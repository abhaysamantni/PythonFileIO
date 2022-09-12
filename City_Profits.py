city_data = open('CityProfits.txt', 'r')
city_name = city_data.readline().rstrip('\n')
while city_name != '':
    q1_profit = float(city_data.readline())
    q2_profit = float(city_data.readline())
    q3_profit = float(city_data.readline())
    tot_profit = q1_profit + q2_profit + q3_profit
    print(city_name, "profit is $", tot_profit)
    city_name = city_data.readline().rstrip('\n')
city_data.close()