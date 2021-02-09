from random import randint
# configuration of the number & player tries.
secret_number = randint(0, 10)
tries = 3
counter = 0
# number input and while loop with if else conditions.
guess = int(input('Please enter the number between 0 and 10:'))
while guess != secret_number:
    if guess < secret_number:
         print('TOO LOW')
    else:
         print('TOO HIGH')
    counter += 1
    print(f'you have used {counter} tries')
    if counter == tries:
        break
    guess = int(input('Please try AGAIN ....'))

if counter < tries :
    print('YOU WON')
else:
    print('YOU LOSE')
