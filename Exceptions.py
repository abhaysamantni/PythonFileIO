try:
   city_data = open('CityProfits2.txt', 'r')
   q1_profit = float(city_data.readline())
   city_data.close()
except FileNotFoundError:
   print("Could not find CityProfit2.txt in current directory")
except ValueError:
   print("No data found in teh file")