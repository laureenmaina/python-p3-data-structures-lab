spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]
# quiz 1
def get_names(spicy_foods):
  names = [food['name'] for food in 
spicy_foods]
  return names

print(get_names(spicy_foods))

# quiz 2
def get_spiciest_foods(spicy_foods):
  spiciest_foods = [food for food in spicy_foods 
                    if food['heat_level'] > 5]
  return spiciest_foods

print(get_spiciest_foods(spicy_foods))

# quiz 3
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food['name']
        cuisine = food['cuisine']
        heat_level = '🌶' * food['heat_level']
        print(f"{name} ({cuisine}) | Heat Level: {heat_level}")

print_spicy_foods(spicy_foods)

# quiz 4
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
   for food in spicy_foods:
       if food['cuisine']==cuisine:
           return food
print(get_spicy_food_by_cuisine(spicy_foods, "American"))

# quiz 5
def print_spiciest_foods(spicy_foods): 
      for food in spicy_foods:
        name = food['name']
        cuisine = food['cuisine']
        heat_level = '🌶' * food['heat_level']
        if food['heat_level'] >5:
            print(f"{name} ({cuisine}) | Heat Level: {heat_level}")

print(print_spiciest_foods(spicy_foods))
    
# quiz 6
def get_average_heat_level(spicy_foods):
  total_heat_level=sum(food['heat_level'] for food in spicy_foods)
  number_of_foods = len(spicy_foods)
  average_heat = total_heat_level / number_of_foods
  return int(average_heat)
  
print(get_average_heat_level(spicy_foods))

# quiz 7
def create_spicy_food(spicy_foods,spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
spicy_foods = [
  {
      "name": "Green Curry",
      "cuisine": "Thai",
      "heat_level": 9,
  },
  {
      "name": "Buffalo Wings",
      "cuisine": "American",
      "heat_level": 3,
  },
  {
      "name": "Mapo Tofu",
      "cuisine": "Sichuan",
      "heat_level": 6,
  },
]

spicy_food = {
    'name': 'Griot',
    'cuisine': 'Haitian',
    'heat_level': 10,
}

print(create_spicy_food(spicy_foods,spicy_food))

