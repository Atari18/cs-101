from .utils import *
from .utils import format_text

USER_PROMPT = format_text("Please select an option number:", new_line=False)
INVALID_OPTION_MESSAGE = format_text("⚠️ Invalid option ⚠️", decorated=True)
MEMBER_PURCHASE_MESSAGE = format_text("🪪 Member card purchased successfully! 🪪", decorated=True)
MEMBER_CANCEL_MESSAGE = format_text("❌ Member card purchase cancelled ❌", decorated=True)

OPTIONS = [
    "1. Purchase Train Tickets",
    "2. Purchase Member Card",
    "1. Purchase Member Card",
    "2. Cancel Purchase"
]

member = False
ticket_prices = [75, 90, 145]

MENU_OPTIONS = format_text("\n".join(OPTIONS[:2]))
MEMBER_OPTIONS = format_text("\n".join(OPTIONS[2:4]))

def user_input_validation(input_range_list, options):
    print_cbc(USER_PROMPT)
    user_input = input("")
    while not check_input(user_input, input_range_list):
        print_cbc(INVALID_OPTION_MESSAGE, RED)
        print_cbc(options)
        print_cbc(USER_PROMPT)
        user_input = input("")
    return user_input

def welcome_message():
    return format_text("---- Ticket Machine™ ----")

def main_menu_display():
    menu_header = format_text("Main Menu", decorated=True)
    return f"{menu_header}\n{MENU_OPTIONS}"

def member_card_display():
    member_message = format_text("Welcome to the Member Card program!", decorated=True)
    discount_message = format_text("Get 50% off all tickets!")
    return f"{member_message}\n{discount_message}\n{MEMBER_OPTIONS}"

def member_card_prompt():
    global member
    user_input = user_input_validation(["1", "2"], MEMBER_OPTIONS)
    if user_input == "1":
        print_cbc(MEMBER_PURCHASE_MESSAGE, GREEN)
        member = True
    else:
        print_cbc(MEMBER_CANCEL_MESSAGE, RED)

def main_menu_prompt():
    user_input = user_input_validation(["1","2"], MENU_OPTIONS)
    if user_input == "1":
        return True
    else:
        return False

def discount_check():
    new_ticket_prices = []
    if member:
        for price in ticket_prices:
            price = price * 0.5
            new_ticket_prices.append(price)
    return new_ticket_prices
