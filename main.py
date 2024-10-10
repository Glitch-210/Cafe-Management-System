print("Welcome To our Restaurant!\nHere is the menu:-")
print("Pizza - Rs.100")
print("Sandwich - Rs.90")
print("French Fries - Rs.80")
print("Burger - Rs.150")
print("Cold Coffee - Rs.80")
print("Water Bottle - Rs.20")
print("Cold Drinks - Rs.20")
print("Meal(Burger,Fries,Pepsi) - Rs.220")
print("")
menu = {
    "pizza" : 100,
    "sandwich" : 90,
    "french fries" : 80,
    "burger" : 150,
    "cold coffee" : 80,
    "water bottle" : 20,
    "cold drinks" : 20,
    "meal" : 220
}

reply = input("What do you want to order? ")
total = 0

if(reply.lower() in menu ):
    print(f"Order of {reply} has been added!")
    total += menu[reply]
    ask = (input(f"Do you want anything else?(Yes/No) "))
    if(ask.lower() == "yes" or ask.startswith("y")): 
        item = input("What do you want to order? ")
        if item in menu:
            total += menu[item]
            print(f"Order of {item} has been added!")
            print(f"{reply} : {menu[reply]}\n{item} : {menu[item]}")
        else:
            print("Sorry! we didn't understand what you are trying to say")
    else:
        breakpoint
else:
    print("Sorry! we didn't understand what you are trying to say")



print(f"Total amount to pay: {total} ")