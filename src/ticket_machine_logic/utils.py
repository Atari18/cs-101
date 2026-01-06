# Import Libraries
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

def format_text(text: str, width: int=40, decorated: bool=False):
    """
    Center's text with the width of 40 and adds a border if specified.
    Args:
        text (str): The text to be formatted.
        width (int): The width of the formatted text.
        decorated (bool): Whether to add a border around the text.

    Returns:
        The formatted text.
    """
    visible_text = re.sub(r'\033\[[0-9;]*m', '', text)
    padding = max(0, (width - len(visible_text)) // 2)
    
    formatted_text = f"{' ' * padding}{text}"
    if decorated:
        border = "=" * width
        formatted_text = f"\n{border}\n{formatted_text}\n{border}"

    return formatted_text

def check_input(input_str, input_range):
    """
    Checks whether a given input string is a valid representation of a value
    within a specified range or collection.

    Args:
        input_str (str): The input string to check.
        input_range (Union[range, Iterable]): The range or collection to validate
            the input string against.

    Returns:
        bool: True if the input string corresponds to a valid value within the
        specified range or collection, False otherwise.
    """
    if not input_str.isdigit():
        return False
    
    val = int(input_str)
    if isinstance(input_range, range):
        return val in input_range
    
    return input_str in map(str, input_range)

def print_cbc(text, color=None, delay=0.01):
    """
    The print_character_by_character function prints text with color and delay for a more
    terminal-based feel,handling ANSI escape sequences.

    Args:
        text (str): The text to be printed.
        color (str, optional): ANSI escape sequence for color. Defaults to None.
        delay (float, optional): Delay between characters in seconds. Defaults to 0.01.
    """
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