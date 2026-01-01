from .utils import *

USER_PROMPT = format_text("Please select an option number:", new_line=False)
INVALID_OPTION_MESSAGE = format_text("⚠️ Invalid option ⚠️", decorated=True)

OPTIONS = [
    "Purchase Train Tickets",
    "Purchase Member Card"
]

FORMATED_OPTIONS = format_options(OPTIONS)
MENU_OPTIONS = "".join(FORMATED_OPTIONS[:2])

def welcome_message():
    return format_text("---- Ticket Machine™ ----")

def main_menu_display():
    menu_header = format_text("Main Menu", decorated=True)
    return f"{menu_header}\n{MENU_OPTIONS}"

def main_menu_prompt():
    print_cbc(USER_PROMPT)
    menu_input = input("")
    while not check_input(menu_input, ["1","2"]):
        print_cbc(INVALID_OPTION_MESSAGE, RED)
        print_cbc(MENU_OPTIONS)
        print_cbc(USER_PROMPT)
        menu_input = input("")
    return menu_input