from art import logo_a
import os
clear = lambda: os.system('cls')
print(logo_a)

bids = {}


def finding_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ''
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if highest_bid < bid_amount:
            highest_bid = bid_amount
            winner = bidder
    print(f'The winner is {winner} with a bid of ${highest_bid}')
while True:
    name = input('What is your name? ')
    price = int(input('What is your bid? R$'))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or no'.\n").lower()[0]
    if should_continue == 'n':
        finding_highest_bidder(bids)
        break
    elif should_continue == 'y':
        clear()