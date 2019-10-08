secret_number = 11
guess_count = 0
guess_limit = 4
while guess_count < guess_limit :
    Guess = int(input('Guess: '))
    guess_count += 1
    if Guess == secret_number:
        print('You won!')
        break
else:
    print("You failed!")

