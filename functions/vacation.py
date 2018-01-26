# 
def distance_from_zero(s):
  if(type(s)==type(1) or type(s)==type(1.1)):
    return abs(s)
  else:
    return "Nope"

# vacation
def hotel_cost(nights):
  cost_night = 140
  return cost_night * nights

def plane_ride_cost(city):
  if(city=="Charlotte"):
    return 183
  elif(city=="Tampa"):
    return 220
  elif(city=="Pittsburgh"):
    return 222
  elif(city=="Los Angeles"):
    return 475

def rental_car_cost(days):
  cost_car_day = 40
  cost_off=0
  if(days>6):
  	cost_off = 50
  elif(days>2):
    cost_off=20

  return days * cost_car_day - cost_off

def trip_cost(city, days, spending_money):
  return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print trip_cost("Los Angeles", 5, 600)
