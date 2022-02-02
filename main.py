cost = 0.00
bill = 1
order = []
sandwhich = input("Would you like a chicken, beef, or tofu sandwhich?: ")
if sandwhich == "chicken":
  print("You picked chicken")
  cost = 5.25
  order.append(sandwhich)
elif sandwhich == "beef":
  print("You picked beef")
  cost = 6.25
  order.append(sandwhich)
elif sandwhich == "tofu":
  print("You picked tofu")
  cost = 5.75
  order.append(sandwhich)
else: 
  print("We do not carry", sandwhich)

beverage = input("Would you like a beverage?: ")
if beverage == "yes":
  bill = bill + 1
  sizeb = input("Small, Medium, or Large?: ")
  if sizeb == "small":
    beverage = "small drink"
    print("You picked small")
    cost = cost + 1.00
    order.append(beverage) 
  elif sizeb == "medium":
    beverage = "medium drink"
    print("You picked medium")
    cost = cost + 1.75
    order.append(beverage) 
  elif sizeb == "large":
    beverage = "large drink"
    print("You picked large")
    cost = cost + 2.25
    order.append(beverage) 
  else:
    print(sizeb, "is not a valid response")
elif beverage == "no":
  print("You don't want a beverage")
  beverage = ""
else: 
  print(beverage, "is not a valid response")

fries = input("Would you like some french fries?: ")
if fries == "yes":
  bill = bill + 1
  sizef = input("Small, Medium, or Large?: ")
  if sizef == "small":
    sure = input("Would you like to megasize your fries to the large size for only one more dollar?:" )
    if sure == "yes":
      fries = "large fries"
      print("You picked large")
      cost = cost + 2.00
      order.append(fries) 
    else:
      fries = "small fries"
      print("You picked small")
      cost = cost + 1.00
      order.append(fries) 
  elif sizef == "medium":
    fries = "medium fries"
    print("You picked medium")
    cost = cost + 1.50
    order.append(fries) 
  elif sizef == "large":
    print("You picked Large")
    cost = cost + 2.00
    order.append(fries)
  else:
    print(sizef, "is not a valid response")
elif fries == "no":
  print("You chose no fries")
  fries = ""
else:
  print(fries, "is not a valid response")

ketchup = int(input("How many ketchup pakcets would you like?: "))
cost = cost + (ketchup * 0.25)
if bill == 3:
  cost = cost - 1.00
print("You ordered a", order)


print("Your total cost is $"+str(cost))
