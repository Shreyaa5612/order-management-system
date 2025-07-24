from menu import menuitems
import datetime
def saving_order(order,grandtotal):
    try:
        with open("orders.txt","r")as file:
            content=file.read()
            order_count=content.lower().count("order #")
    except FileNotFoundError:
        order_count=0
    order_number=order_count+1
    with open("orders.txt","a")as file:
        file.write(f"\norder #{order_number}")
        file.write("\nnew_order")
        for item,quantity in order.items():
            price=menuitems[item]*quantity
            file.write(f"\n{item} x {quantity}= rs{price}")
        file.write(f"\ngrandtotal={grandtotal}")
        file.write(f"\norder placed on {datetime.datetime.now()}\n")
        file.write("-"*20+"\n")
        print(f"\nyour order (order number:#{order_number}) is saved successfully")
        print("-"*20+"\n")