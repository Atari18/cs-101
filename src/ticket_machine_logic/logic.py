from PIL import Image
from .utils import format_text, print_cbc, check_input, GREEN, RED, YELLOW

# Constants for cleaner configuration
TICKET_PRICES = [75, 90, 145]
MEMBER_DISCOUNT = 0.5
USER_PROMPT = format_text("Please select an option number:", new_line=False)

MESSAGES = {
    "invalid": format_text("⚠️ Invalid option ⚠️", decorated=True),
    "success": format_text("🪪 Member card purchased successfully! 🪪", decorated=True),
    "cancel": format_text("❌ Member card purchase cancelled ❌", decorated=True),
    "welcome": format_text("---- Ticket Machine™ ----"),
    "member_intro": f"{format_text('Welcome to the Member Card program!', decorated=True)}\n"
                    f"{format_text('Get 50% off all tickets!')}"
}

OPTIONS = {
    "main": format_text("1. Purchase Train Tickets\n2. Purchase Member Card"),
    "member": format_text("1. Purchase Member Card\n2. Cancel Purchase")
}

state = {"is_member": False}

def user_input_validation(valid_range, options_display):
    while True:
        print_cbc(options_display)
        print_cbc(USER_PROMPT)
        user_input = input("").strip()
        if check_input(user_input, valid_range):
            return user_input
        print_cbc(MESSAGES["invalid"], RED)

def member_card_prompt():
    if user_input_validation(["1", "2"], MESSAGES["member_intro"] + "\n" + OPTIONS["member"]) == "1":
        print_cbc(MESSAGES["success"], GREEN)
        state["is_member"] = True
    else:
        print_cbc(MESSAGES["cancel"], RED)

def show_train_stations():
    try:
        with Image.open("assets/images/train_station_map.jpg") as img:
            img.show()
    except FileNotFoundError:
        print_cbc("\n[Error] Map file not found.", RED)

def get_discounted_prices():
    factor = MEMBER_DISCOUNT if state["is_member"] else 1.0
    return [price * factor for price in TICKET_PRICES]
