#  A LIST IN A DICTIONARY
# Store information about a pizza being ordered
pizza = { # dictionary that holds information about a pizza that has been ordered.
    'crust': 'thick', # key 'toppings'
    'toppings': ['mushrooms','extra cheese'],
}
# Summarize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza" + # summarize the order before building pizza.
      "with the following toppings:")
for topping in pizza['toppings']: # print toppings, we do a for loop using the key 'toppings'.
    print("\t" + topping)