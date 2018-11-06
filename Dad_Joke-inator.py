from requests import *
from pyfiglet import figlet_format
from random import randint

url = "https://icanhazdadjoke.com/search"

print(figlet_format("Welcome to Dad Joke-inator!"))
query = input("I've got awesome jokes about pretty much everything. Gimme a topic: ")

res = get(url,headers={"Accept":"application/json"},params={"term":query})
data = res.json()
data = data["results"]

if len(data) == 0:
    print("Sorry, kid, I got nothing.")
elif len(data) == 1:
    print(f"I've got one joke about {query}. Here it is:")
    print(data["joke"])
else:
    print(f"I've got {str(len(data))} jokes about {query}. Here's one:")
    num = randint(0, len(data))
    print(data[num]["joke"])