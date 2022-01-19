cost = 0.00
bill = 1
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
  bill = bill + 1
  sizeb = input("Small, Medium, or Large?: ")
  if sizeb == "small":
    print("You picked small")
    cost = cost + 1.00
  elif sizeb == "medium":
    print("You picked medium")
    cost = cost + 1.75
  else:
    print("You picked large")
    cost = cost + 2.25
else:
  print("You picked no beverage")
  beverage = ""

fries = input("Would you like some french fries?: ")
if fries == "yes":
  bill = bill + 1
  sizef = input("Small, Medium, or Large?: ")
  if sizef == "small":
    sure = input("Would you like to megasize your fries to the large size for only one more dollar?:" )
    if sure == "yes":
      print("You picked large")
      cost = cost + 2.00
    else:
      print("You picked small")
      cost = cost + 1.00
  elif sizef == "medium":
    print("You picked medium")
    cost = cost + 1.50
  else:
    print("You picked Large")
    cost = cost + 2.00
else: 
  print("You chose no fries")
  fries = ""

ketchup = int(input("How many ketchup pakcets would you like?: "))
cost = cost + (ketchup * 0.25)
if bill == 3:
  cost = cost - 1.00
print("You ordered", sandwhich, beverage, fries)


print("Your total cost is $"+str(cost))
