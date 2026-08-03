import logo

print(logo)
print("Welcome to the secret auction program.")

users = {}
auction = True

def find_highest_bid(user_dict):
    winner = ""
    highest_bid = 0
    for user in user_dict:
        bid = user_dict[user]
        if bid > highest_bid:
            highest_bid = bid
            winner = user

    print(f"The winner was {winner} with a bid of ${highest_bid}")

while auction:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    users[name] = bid

    more_bidders = input("Are there any other bidders? Type \"Yes\" or \"No\": ").lower().strip()

    print("\n" * 20)

    if more_bidders == "no":
        auction = False
        find_highest_bid(users)
