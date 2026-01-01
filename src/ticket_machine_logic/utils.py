import time
import sys

# ANSI Color Codes
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
RESET = "\033[0m"

def format_text(text, width=40, decorated=False, new_line=True):
    centered_text = text.center(width)
    if decorated:
        line = "=" * width
        return f"\n{line}\n{centered_text}\n{line}"
    else:
        if new_line:
            return f"\n{centered_text}\n"
        else:
            return f"\n{centered_text}"

def format_options(options):
    formatted_options = []
    for index, text in enumerate(options, start=1):
        option_str = format_text(f"{index}. {text}")
        formatted_options.append(option_str)
    return formatted_options

def check_input(input_str, input_range):
    if input_str.isdigit() and input_str in input_range:
        return True
    else:
        return False

def print_cbc(text, color=None, delay=0.02):
    if color:
        sys.stdout.write(color)

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

    if color:
        sys.stdout.write(RESET)