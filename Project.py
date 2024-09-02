Menu={ 
    'Zinger Burger':320,
    "BBQ Sandwitch":350,
    "Zinger Shwarma":190,
    "Pizza":1000,
    "Chicken Roll":150,

}

#Greet
print("Welcome To F&F Restaurant")
print("Zinger Burger:Rs 320\nBBQ Sandwitch:Rs350\nZinger Shwarma:Rs190\nPizza: Rs1000\nChicken Roll: Rs150")

total_item=0

item_1=input("Place your Order:")

if item_1 in Menu:
    total_item+=Menu[item_1]
    print(f"your order {item_1} is placed")

else:
    print("this item is not avail right now")

another_order=input("do you want another item (yes/No)")
if another_order=="yes":
    item_2=input("place your other order:")
    if item_2 in Menu:
     total_item+=Menu[item_2]
     print(f"{item_2} is ordered")
    else:
       print(f"this item {item_2} is not avail right now")

print("total amount to pay{total_item}")
