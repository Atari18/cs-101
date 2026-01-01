import sys
import os
from src.ticket_machine_logic.logic import (
    MESSAGES, OPTIONS, state, member_card_prompt, 
    show_train_stations, user_input_validation
)
from src.ticket_machine_logic.utils import print_cbc, GREEN, YELLOW

def run_app():
    while True:
        print_cbc(MESSAGES["welcome"], GREEN)
        choice = user_input_validation(["1", "2"], OPTIONS["main"])
        
        if choice == "1":
            show_train_stations()
            # select_station() logic would go here
            break # Exit after purchase or loop back
        else:
            member_card_prompt()

if __name__ == "__main__":
    try:
        run_app()
    except KeyboardInterrupt:
        print_cbc("\n\nThank you for using Ticket Machine™. Goodbye!", YELLOW)


