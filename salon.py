hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_price = 0
for i in prices:
  total_price += i
average_price = total_price/(len(hairstyles))
print("Average Price:",average_price)
new_prices = [i - 5 for i in prices]
print(new_prices)
total_revenue = 0
for i in range(0, len(hairstyles) - 1):
  total_revenue = prices[i] + last_week[i]
print("Total revenue:", total_revenue)
average_daily_revenue = total_revenue/7
cuts_under_30 = [hairstyles[i] for i in range(0,len(new_prices) - 1) if new_prices[i] < 30]
print(cuts_under_30)



