from marvel import Marvel
from keys import PUBLIC_KEY, PRIVATE_KEY

marvel = Marvel(PUBLIC_KEY=PUBLIC_KEY, 
                PRIVATE_KEY=PRIVATE_KEY)

characters = marvel.characters

my_char = characters.all(nameStartsWith="Captain")["data"]["results"]

for char in my_char:
    print(char["id"], char["name"])
    for comic in char["comics"]["items"]:
        print(comic["name"])
    print("---------------------")
        