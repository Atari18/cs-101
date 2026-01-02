"""
Entry point for the Ticket Machine™ application.

This module initializes the main loop and handles the high-level 
application flow and user interruptions.
"""
from src.ticket_machine_logic.logic import (
    MESSAGES, OPTIONS, member_card_prompt,
    show_train_stations, get_valid_input, select_station, end_program
)
from src.ticket_machine_logic.utils import print_cbc, GREEN, YELLOW

def run_app() -> None:
    """
    The main application loop that keeps the machine running until 
    the user completes a purchase or exits.
    """
    while True:
        print_cbc(MESSAGES["welcome"], GREEN)
        print_cbc(MESSAGES["menu_title"])
        
        choice = get_valid_input(["1", "2"], OPTIONS["main"])
    
        if choice == "1":
            show_train_stations()
            select_station()
            end_program()
        else:
            member_card_prompt()

if __name__ == "__main__":
    try:
        run_app()
    except (KeyboardInterrupt, SystemExit):
        print_cbc("\nGoodbye!", YELLOW)
