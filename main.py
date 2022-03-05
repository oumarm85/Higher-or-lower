import random
import art
from game_data import data
from replit import clear


def compare(answer, a_followers, b_followers):
    """Compare the answer answer player provides against the correct answer"""
    if a_followers > b_followers and answer == 'a':
        return True
    elif a_followers > b_followers and answer == 'b':
        return False
    elif b_followers > a_followers and answer == 'a':
        return False
    elif b_followers > a_followers and answer == 'b':
        return True


def set_account():
    """Return a random set of data to be used in the game"""
    return random.choice(data)


def game():
    print(art.logo)
    score = 0
    play = 'y'
    set_a = set_account()
    set_b = set_account()

    while play == 'y':
        clear()
        print(art.logo)
        print(f"Your current score is: {score}")
        set_a = set_b
        set_b = set_account()

        a_followers = set_a['follower_count']
        b_followers = set_b['follower_count']

        print(f'Compare A: {set_a["name"]}, a {set_a["description"]}, from {set_a["country"]}.')
        print(art.vs)
        print(f'Against B : {set_b["name"]}, a {set_b["description"]}, from {set_b["country"]}.')

        answer = input("Who has more followers? Enter 'A' or 'B': ").lower()

        is_correct = compare(answer, a_followers, b_followers)

        if is_correct == True:
            score += 1
            print(f"Correct!")
        else:
            print(f"Wrong! Final score was {score}.")
            play = input("Do you want to play again? 'Y' or 'N': ").lower()


game()