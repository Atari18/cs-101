from PIL import Image
from .utils import (
    format_text, print_cbc, check_input, 
    GREEN, RED, YELLOW, BLUE, RESET
)

# Configuration Constants
MEMBER_DISCOUNT = 0.5
RETURN_MULTIPLIER = 1.5
USER_PROMPT = "Please select an option number: "

# Grouping station data into a list of dictionaries for better maintainability
STATIONS = [
    {"name": "Rivenhester", "price": 75.0},
    {"name": "Starling Point", "price": 90.0},
    {"name": "Frosthaven Crossing", "price": 145.0}
]

MESSAGES = {
    "invalid": format_text("⚠️ Invalid option ⚠️", decorated=True),
    "success": format_text("🪪 Member card active! 🪪", decorated=True),
    "cancel": format_text("❌ Purchase cancelled ❌", decorated=True),
    "welcome": format_text("---- Ticket Machine™ ----"),
    "menu_title": format_text("Main Menu", decorated=True),
    "station_menu": format_text("Select Station", decorated=True, width=25),
    "farewell": format_text("Thank you for using Ticket Machine™", decorated=True),
    "member_intro": f"{format_text('Member Card Program', decorated=True)}\n{format_text('Save 50% on all tickets!')}"
}

OPTIONS = {
    "main": "1. Purchase Train Tickets\n2. Purchase Member Card",
    "member": "1. Purchase Member Card\n2. Cancel Purchase",
    "stations": "\n".join([f"{i+1}. {s['name']}" for i, s in enumerate(STATIONS)]),
    "return": "\nTrip Type:\n1. Return (1.5x)\n2. One-way\n"
}

# Application State
state = {"is_member": False}


def get_valid_input(valid_options, display_text="", show_prompt=True):
    while True:
        if display_text:
            print_cbc(display_text)
        
        if show_prompt:
            print_cbc(USER_PROMPT)

        user_input = input("").strip()
        if check_input(user_input, valid_options):
            return user_input

        print_cbc(MESSAGES["invalid"], RED)

def member_card_prompt():
    choice = get_valid_input(["1", "2"], f"{MESSAGES['member_intro']}\n{OPTIONS['member']}")
    if choice == "1":
        print_cbc(MESSAGES["success"], GREEN)
        state["is_member"] = True
    else:
        print_cbc(MESSAGES["cancel"], RED)

def show_train_stations():
    try:
        Image.open("assets/images/train_station_map.jpg").show()
    except Exception:
        print_cbc("\n[Error] Could not load station map.", RED)

def select_station():
    print_cbc(MESSAGES["station_menu"])
    idx = int(get_valid_input(["1", "2", "3"], OPTIONS["stations"])) - 1
    station = STATIONS[idx]

    print_cbc(f"\nTickets to {station['name']} (1-99): ")
    qty = int(get_valid_input(range(1, 100), "", show_prompt=False))

    is_return = get_valid_input(["1", "2"], OPTIONS["return"], False) == "1"
    
    # Calculate
    unit = station["price"] * (MEMBER_DISCOUNT if state["is_member"] else 1.0)
    total = unit * qty * (RETURN_MULTIPLIER if is_return else 1.0)

    # Receipt construction with centering and color
    member_tag = f" {BLUE}(Member){RESET}" if state["is_member"] else ""
    
    receipt_content = [
        format_text("OFFICIAL RECEIPT", decorated=True),
        format_text(f"Station: {station['name']}"),
        format_text(f"Quantity: {qty}"),
        format_text(f"Unit Price: £{unit:.2f}{member_tag}"),
        format_text(f"Trip: {'Return' if is_return else 'One-way'}"),
        format_text("-" * 20),
        format_text(f"TOTAL: £{total:.2f}"),
        format_text("Safe travels!")
    ]
    
    print_cbc("\n".join(receipt_content))

def end_program():
    print_cbc(MESSAGES["farewell"], YELLOW)
    exit()
