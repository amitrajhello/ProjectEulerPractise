import random

my_number = random.randint(1, 10)

count = 4
while count>=0:
    guess = int(input('enter a lucky number between "1" and "10" to win: '))
    count -= 1
    if(count<1):
        print('oops! you lose!')
        break
    if guess == my_number:
        print(f'Cheers! {guess} is correct number! you won!')
        break
        a = False
    else:
        if abs(guess - my_number) > 3:
            print(f'your number is far away, you have "{count}" chances left')
        else:
            print(f'you are getting close! , you have "{count}" chances left')


