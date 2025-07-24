from menu import menuitems
from show_menu import view_menu
def taking_order():
    view_menu()
    order={}
    while True:
        item=input("what item do you want: ").lower()
        if item in menuitems:
            quantity = int(input("how many quantity do you want:"))
            if item in order:
                order[item]+=quantity
            else:
                order[item]=quantity
        else:
            print("sorry,item not in the menu list.please order again")
        choice = input("do you want anything else: type yes/no:")
        if choice == 'no':
            print(f"you have ordered : {order}")
            break
    return order







