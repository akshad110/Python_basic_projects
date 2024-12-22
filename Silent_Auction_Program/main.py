import os

def find_winner(bidder_details):
    highest_bid = 0
    winner = ""
    for bidder in bidder_details:
      bidding_price = bidder_details[bidder]
      if bidding_price > highest_bid:
             highest_bid = bidding_price
             winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")

bidder={}
flag = False
while not flag:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid price: "))
    bidder[name] = bid
    more_bidder = input("Are there any more bidders? Type 'yes' or 'no': ").lower()
    if more_bidder == "no":
        flag = True
        find_winner(bidder)
    elif more_bidder == "yes":
        os.system('cls')

        