import sys
import os
from src.ticket_machine_logic.logic import *

# Telling python to look inside the 'src' folder for my packages
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))



def start_screen():
    print_cbc(welcome_message(), GREEN)
    print_cbc(main_menu_display())

if __name__ == "__main__":
    start_screen()

    if main_menu_prompt():
        pass
    else:
        print_cbc(member_card_display(), YELLOW)
        member_card_prompt()


    start_screen()


