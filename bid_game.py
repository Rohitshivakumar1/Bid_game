from replit import clear

from art import logo

print(logo)

bids = {}
bidding_finished = False


higest_bid = 0
def find_highest_bidder(bidding_record):
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > higest_bid:
            higest_bid = bid_amount
            winner = bidder
        print(f"The winner is {winner} with bid amout of {higest_bid}")
    



while not bidding_finished:
    name = input("what is your name?")
    price = int(input("what is ur bid $"))
    bids[name] = price
    should_coun = input("are there any other bidders Yes or No")
    if should_coun == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_coun == "yes":
        clear()
