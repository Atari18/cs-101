import time
import sys
import re

# ANSI Color Codes
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
STRIKETHROUGH = "\033[9m"
RESET = "\033[0m"

def format_text(text, width=40, decorated=False):
    # Strip ANSI codes to calculate visible length
    visible_text = re.sub(r'\033\[[0-9;]*m', '', text)
    padding = max(0, (width - len(visible_text)) // 2)
    
    formatted_text = f"{' ' * padding}{text}"

    if decorated:
        border = "=" * width
        formatted_text = f"\n{border}\n{formatted_text}\n{border}"

    return formatted_text

def check_input(input_str, input_range):
    if not input_str.isdigit():
        return False
    
    val = int(input_str)
    if isinstance(input_range, range):
        return val in input_range
    
    return input_str in map(str, input_range)

def print_cbc(text, color=None, delay=0.01):
    if text is None:
        return

    lines = str(text).splitlines()
    for line in lines:
        if color:
            sys.stdout.write(color)

        if "\033[" in line:
            sys.stdout.write(line)
        else:
            for char in line:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(delay)

        sys.stdout.write(RESET + "\n")
        sys.stdout.flush()