from termcolor import colored

words = "hello, there"
text = colored("HELLO", color="magenta", on_color="on_cyan", attrs=["blink"])
print(text)