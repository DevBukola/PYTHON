import pyfiglet
from termcolor import colored

msg = input("What would you like to print? ")
color = input("What color? ")

valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan")

if color not in valid_colors:
    color = "magenta"
ascii_art = pyfiglet.figlet_format(msg)
colored_ascii = colored(ascii_art, color=color, attrs=["blink"])
print(colored_ascii)