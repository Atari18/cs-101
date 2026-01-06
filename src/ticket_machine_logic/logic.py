# Import libraries
from PIL import Image, UnidentifiedImageError
from .utils import (
    format_text, print_cbc, check_input, 
    GREEN, RED, YELLOW, BLUE, RESET
)

# Configuration Constants
MEMBER_DISCOUNT = 0.5
RETURN_MULTIPLIER = 1.5
USER_PROMPT = "Please select an option number: "
MAP_IMAGE_PATH = "assets/images/train_station_map.jpg"

# The name of the stations relative to the price of the ticket in a list of dictionary's
STATIONS = [
    {"name": "Rivenhester", "price": 75.0},
    {"name": "Starling Point", "price": 90.0},
    {"name": "Frosthaven Crossing", "price": 145.0}
]

# Formatted Messages
MESSAGES = {
    "invalid": format_text("⚠️ Invalid option ⚠️", decorated=True),
    "success": format_text("🪪 Member card active! 🪪", decorated=True),
    "cancel": format_text("❌ Purchase cancelled ❌", decorated=True),
    "welcome": format_text("---- Ticket Machine™ ----"),
    "menu_title": format_text("Main Menu", decorated=True),
    "station_menu": format_text("Select Station", decorated=True, width=25),
    "farewell": format_text("Thank you for using Ticket Machine™", decorated=True),
    "member_intro": f"{format_text('Member Card Program', decorated=True)}\n"
                    f"{format_text('Save 50% on all tickets!')}"
}

# List of options to be used as arguments for get_valid_input
OPTIONS = {
    "main": "1. Purchase Train Tickets\n2. Purchase Member Card",
    "member": "1. Purchase Member Card\n2. Cancel Purchase",
    "stations": "\n".join([f"{i+1}. {s['name']}" for i, s in enumerate(STATIONS)]),
    "return": "\nTrip Type:\n1. Return (1.5x)\n2. One-way\n"
}

# Dictionary to store the state of the user's membership
state = {"is_member": False}


def get_valid_input(valid_options: list[str], display_text: str="", show_prompt:bool=True):
    """
    Gets valid user input from a predefined set of options.

    This function continually prompts the user for input until a valid value
    from the specified options is provided.

    Args:
        valid_options (list[str]): A list of valid input options to be matched
            against the user's input.
        display_text (str): Text to display to the user before receiving input.
            Defaults to an empty string.
        show_prompt (bool, optional): Whether to show an additional user input prompt.
            Defaults to True.

    Returns:
        str: The validated user input that matches one of the valid options.
    """
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
    """
    Prompts the user to select a membership status and updates the Membership state accordingly.

    This function interacts with the user by displaying membership options and receiving their
    input. Based on the input provided, it sets the membership status in the global variable "state" and provides
    feedback to the user.

    Raises:
        Any error raised by the `get_valid_input`, `print_cbc`, or any global dependencies.

    """
    choice = get_valid_input(["1", "2"], f"{MESSAGES['member_intro']}\n{OPTIONS['member']}")
    if choice == "1":
        print_cbc(MESSAGES["success"], GREEN)
        state["is_member"] = True
    else:
        print_cbc(MESSAGES["cancel"], RED)

def show_train_stations():
    """
    Displays the train station map image if available.

    Raises:
        Exception: If the image cannot be opened or displayed.

    """
    try:
        with Image.open(MAP_IMAGE_PATH) as img:
            img.show()
    except (FileNotFoundError, UnidentifiedImageError):
        print_cbc("\n[Error] Could not find or load the station map image file.", RED)
    except Exception as e:
        print_cbc(f"\n[Error] An unexpected error occurred: {e}", RED)

def select_station():
    """
    Print the list of available stations and prompt the user to select one.
    Ask how many tickets they want to purchase.
    Check if invalid input is provided.
    Ask whether they want the selected ticket to be a return trip.
    Check if invalid input is provided.
    Check if the user is a member.
    Calculate the total cost of the purchase.
    Print the receipt.




    Returns:
        dict: The details of the selected station.
    """
    print_cbc(MESSAGES["station_menu"])
    idx = int(get_valid_input(["1", "2", "3"], OPTIONS["stations"])) - 1
    station = STATIONS[idx]

    print_cbc(f"\nTickets to {station['name']} (1-99): ")
    valid_range = [str(n) for n in range(1, 100)]
    qty = int(get_valid_input(valid_range, "", show_prompt=False))

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
    """Ends the program and prints a farewell message."""
    print_cbc(MESSAGES["farewell"], YELLOW)
    exit()
