from menu import menuitems
def view_menu():
    print("____menu____")
    for item,price in menuitems.items():
        print(f"{item}:rs{price}")
    print("-"*20+"\n")





