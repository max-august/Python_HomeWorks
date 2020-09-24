#This is a guess the number game
import random

#Java 에서 보통 저렇게 씀
guessesTaken = 0
#일반 파이선 유저
guesses_taken = 0

print('Hello! What is your name?')
myName = input()

#The random .randint() Function
number = random.randint(1,20)

#Welcoming the Player
print('Well, ' + myName + ', I am thinking of a number between  1 and 20.')

#Loops
while guessesTaken < 6:
    print('Take a guess.')
    guess = input()
    #int를 넣어야 하는 이유가 넣어햐 하는 값이 숫자로 표기해야 하기 때문만인가요?
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low.')

    if guess > number:
        print('Your guess is too high.')
    
    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed my number in '+ guessesTaken + 'guesses!')

if guess != number:
    number = str(number)
    print('nope. The number i was thinking of was' + number)