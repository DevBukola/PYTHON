import requests
from random import choice
import pyfiglet
from termcolor import colored

header = pyfiglet.figlet_format("DAD JOKE 3000!")
header = colored(header, color="green", attrs=["blink"])
print(header)

user_search = input("Let me tell you a joke! Give me a topic: ")

url = "https://icanhazdadjoke.com/search"
res = requests.get(
    url, 
    headers={"Accept": "application/json"}, 
    params={"term": user_search}
).json()
num_jokes = res["total_jokes"]
results = res["results"]
if num_jokes == 1:
    print(f"I found one joke about {user_search}. Here it is:")
    print(res["results"][0]['joke'])
elif num_jokes > 1:
    print(f"I found {num_jokes} jokes about {user_search}. Here's one:")
    print(choice(results)["joke"])
else:
    print(f"Sorry, couldn't find a joke with your term: {user_search} ")