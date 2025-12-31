import sys
import os

# Telling python to look inside the 'src' folder for my packages
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from ticket_machine_logic.logic import *



if __name__ == "__main__":
    print(func())
