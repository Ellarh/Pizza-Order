print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ").upper()
add_pepperoni = input("Do you want pepperoni? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()
drink = input("Would you like anything to drink? Y or N: ").upper()
dessert = input("Do you want dessert? Y or N ").upper()
bill = 0

if size == "S":
  bill = 15
  if add_pepperoni == "Y":
    bill += 2
  if extra_cheese == "Y":
    bill += 1
  if drink == "Y":
    bill += 4
  if dessert == "Y":
    bill += 5
  print(f"Your final bill is ${bill}")
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
      bill += 3
    if extra_cheese == "Y":
      bill += 1
    if drink == "Y":
      bill += 4
    if dessert == "Y":
      bill += 5
    print(f"Your final bill is ${bill}")
elif size == "L":
    bill = 25
    if add_pepperoni == "Y":
      bill += 3
    if extra_cheese == "Y":
      bill += 1
    if drink == "Y":
      bill += 4
    if dessert == "Y":
      bill += 5
    print(f"Your final bill is ${bill}")
  
else:
  print("You have not placed an order")




