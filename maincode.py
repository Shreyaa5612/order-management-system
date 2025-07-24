from menu import menuitems
from show_menu import view_menu
from take_order import taking_order
from generate_bill import bill_generation
from save_order import saving_order
def main():
    print("WELCOME TO THE FOODIE RESTAURANT")
    while True:
        choice=int(input("1->view menu\n2->take order\n3->exit\nenter your choice:"))
        if choice==1:
            view_menu()
        elif choice==2:
            order=taking_order()
            grandtotal=bill_generation(order)
            saving_order(order,grandtotal)
        elif choice==3:
            print("thank you for visiting....")
            break
        else:
            print("wrong choice entered.please enter again")

if __name__=="__main__":
    main()




