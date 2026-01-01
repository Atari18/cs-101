import sys
import os
from src.ticket_machine_logic.logic import *

# Telling python to look inside the 'src' folder for my packages
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))





if __name__ == "__main__":
    print_cbc(welcome_message(), GREEN)
    print_cbc(main_menu_display())
    main_menu_prompt()
