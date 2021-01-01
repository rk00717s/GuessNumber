from random import randrange

def user_guess(min_guess_limit, max_guess_limit):
    guess_count = 0
    guess = randrange(min_guess_limit, max_guess_limit)
    while(True):
        my_guess = int(input("::: "))
        guess_count +=1
        if(my_guess > guess):
            print("Sry. Your guess is too high to compare.")
        elif(my_guess == guess):
            print(f"Yea!! you{(' finally ' if guess_count >=2 else ' ')}guess the word.")
            break
        elif(my_guess < guess):
            print("Sry. Your guess is too low to compare.")
        else:
            pass

def system_guess(min_guess_limit, max_guess_limit):
    guess_count = 0
    guess = randrange(min_guess_limit, max_guess_limit)
    while True:
        min_guess_limit = min_guess_limit if min_guess_limit<max_guess_limit else max_guess_limit
        max_guess_limit = min_guess_limit if min_guess_limit>max_guess_limit else max_guess_limit
        guess = randrange(min_guess_limit, max_guess_limit) if(min_guess_limit != max_guess_limit) else guess
        my_answer = input(f"Is {guess} is to High(H), to Low(L), or Correct(C) : ").lower()
        guess_count += 1
        if(my_answer == 'h'):
            guess -= 1
            # guess = guess - guess//2
            max_guess_limit = guess
        elif(my_answer == 'c'):
            print(f"Yeepy! I guessed the word correct in {guess_count} tries")
            break
        elif(my_answer == 'l'):
            guess += 1
            # guess = guess + guess//2
            min_guess_limit = guess
        else:
            pass

if __name__ == "__main__":
    min_guess_limit = 1
    max_guess_limit = 10
    preference = input("Do you wanted to guess by Yourself(Y) or by Myself(M) : ").lower()
    if(preference == 'y'):
        user_guess(min_guess_limit, max_guess_limit)
    elif(preference == 'm'):
        system_guess(min_guess_limit, max_guess_limit)
    else:
        pass