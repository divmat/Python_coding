toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
prices = [2, 6, 1, 3, 2, 7, 2]
num_pizzas = len(toppings)
print("We sell", num_pizzas, "different kinds of pizza!")
pizzas = list(zip(prices, toppings))
print(pizzas)
pizzas.sort()
cheapest_pizza = pizzas[0]
priciest_pizza = pizzas[-1]
print("Our cheapest pizza is -",cheapest_pizza)
print("Our priciest pizza is -",priciest_pizza)
three_cheapest = pizzas[:3]
print("Our three cheapest pizzas are-", three_cheapest)
num_two_dollar_slices = prices.count(2)

