from menu import menuitems
from show_menu import view_menu
from take_order import taking_order
def bill_generation(order):
    print("\n____bill____")
    total_price=0
    for item,quantity in order.items():
        price=menuitems[item]*quantity
        total_price+=price
        print(f"{item}x{quantity}=rs{price}")
    tax=total_price*0.05  #5%gst
    grandtotal=total_price+tax
    print("sub_total=",total_price)
    print("gst=5%")
    print("grand_total=",grandtotal)
    print("you have to pay rs",grandtotal)
    print("thank you for your order!")
    print("-"*20+"\n")
    return grandtotal
