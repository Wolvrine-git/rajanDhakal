import random
def roller():
    dice = random.randint(1,6)
    return dice



player=[]
for i in range(1,5):
    name= input(f"Enter {i} player name: ").upper()
    player.append(name)

for i , item in enumerate(player , start=1):
    print(f"{i}. {item}")

while True:
    for i in player:
        print(i , "Turn:")
        input()
        number = roller()
        print(f"{i} = {number}")