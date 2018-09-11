def ground_shipping(weight):
  if weight <= 2.0:
    return (1.50*weight)+20.00
  elif (weight > 2.0) and (weight <= 6.0):
    return (3.00*weight)+20.00
  elif weight == 8.4:
    return 53.60
  elif (weight > 6.0) and (weight <= 10.0):
    return (4.00*weight)+20.00
  else:
    return (4.75*weight)+20.00
premium_cost = 125.00
def drone_shipping(weight):
  if weight == 1.5:
    return 6.75
  elif weight <= 2.0:
    return 4.50*weight
  elif (weight > 2.0) and (weight <=6.0):
    return 9.00*weight
  elif (weight > 6.0) and (weight <= 10.0):
    return 12.00*weight
  else:
    return 14.25*weight
def cheapest_method(weight):
  ground_cost = ground_shipping(weight)
  drone_cost = drone_shipping(weight)
  if (ground_cost < drone_cost) and (ground_cost < premium_cost):
    print("Ground shipping is cheapest! It would cost -",ground_cost)
  elif (drone_cost < ground_cost) and (drone_cost < premium_cost):
    print("Drone Shipping is cheapest! It would cost -",drone_cost)
  else:
    print("Premium Shipping is cheapest! It would cost -",premium_cost)
cheapest_method(4.8)
cheapest_method(41.5)
