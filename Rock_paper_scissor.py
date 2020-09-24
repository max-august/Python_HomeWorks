import random

print("Welcome!")

choices = ['R', 'P', 'S']
computer = random.choice(choices)
player = input('R,P,S!:')

print('computer had', computer)

if player == computer:
    print("Draw")
elif (player=='S' and computer=='p' or 
    player=='R' and computer=='S' or
    player=='P' and computer=='R'):
    print('Win')
else:
    print("lose")