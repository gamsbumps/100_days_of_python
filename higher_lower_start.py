from art import logo_d, vs
from game_data import data
import os
import random

clear = lambda: os.system('cls')

score = 0
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_a = random.choice(data)
guessing_right = True
while guessing_right:
    clear()
    print(logo_d)
    if score > 0:
        print(f"You are right! Current score: {score}.")
    print(f"Compare A: {account_a['name']}, a {account_a['description']} from {account_a['country']}")
    print(vs)
    print(f"Against B: {account_b['name']}, a {account_b['description']} from {account_b['country']}")
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    if account_a['follower_count'] > account_b['follower_count'] and guess == 'A':
        score += 1
        account_b = random.choice(data)
    elif account_b['follower_count'] > account_a['follower_count'] and guess == 'B':
        score += 1
        account_a = account_b
        account_b = random.choice(data)
    else:
        print(f"You lose. Your score was: {score}")
        guessing_right = False
