cost = 0.00
sandwhich = input("Would you like a chicken, beef, or tofu sandwhich?: ")

if sandwhich == "chicken":
  print("You picked chicken")
  cost = 5.25
elif sandwhich == "beef":
  print("You picked beef")
  cost = 6.25
else:
  print("you picked tofu")
  cost = 5.75
beverage = input("Would you like a beverage?: ")
if beverage == "yes":
  size = input("Small, Medium, or Large?: ")
  if size == "small":
    print("You picked small")
    cost = cost + 1.00
  elif size == "medium":
    print("You picked medium")
    cost = cost + 1.75
  else:
    print("You picked large")
    cost = cost + 2.25
else:
  print("You picked no beverage")
print("Your total cost is $"+str(cost))