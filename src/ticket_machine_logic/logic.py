from .utils import _check_user_input

INVALID_CHOICE = "Invalid choice, please try again"

def main_menu():
    option = 0
    print("Welcome to the ticket machine!")
    print("1.Buy Ticket\n2.Buy Membership")
    choice = input("Enter 1 to buy ticket or 2 to buy membership: ")

    while not _check_user_input(choice, [1,2]):
        print(INVALID_CHOICE)
        choice = input("Enter your choice: ")

    if int(choice) == 1:
        buy_ticket()
    else:
        buy_membership()

def buy_membership():
    print("Welcome to the membership program!\nGet 50% off on all tickets!\nMembership price: £100")
    print("1.Purchase membership\n2.Cancel purchase")
    choice_2 = (input("Enter 1 to purchase membership or 2 to cancel purchase:"))

    while not _check_user_input(choice_2, [1,2]):
        print(INVALID_CHOICE)
        choice_2 = (input("Enter 1 to purchase membership or 2 to cancel purchase:"))

    if int(choice_2) == 1:
        print("Membership purchased successfully!")
        main_menu()
    else:
        print("Membership purchase cancelled")
        main_menu()

def buy_ticket():
    print("Welcome to the ticket machine!")