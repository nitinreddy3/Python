import random

random_num = random.randint(1, 10)
guessed_nums = []
allowed_guesses = 5

while  len(guessed_nums) < allowed_guesses:
    guess = input("Guess a number between 1 and 10: ")

    try:
        player_num = int(guess)
    except:
        print("That's not a number")
        break

    if not player_num > 0 or not player_num < 11:
        print("That number is not between 1 and 10 ")
        break

    guessed_nums.append(player_num)

    if player_num == random_num:
        print("You win! My number was {}".format(random_num))
        print("It took you {} tries.".format(len(guessed_nums)))
        break
    else:
        if random_num > player_num:
            print("Nope my number is higher than {}. Guess attempt #{}".format(player_num, len(guessed_nums)))
        else:
            print("Nope my number is lower than {}. Guess attempt #{}".format(player_num, len(guessed_nums)))
        continue

if not random_num in guessed_nums:
    print("Sorry my number was {}.".format(random_num))
