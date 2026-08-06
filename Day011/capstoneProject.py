import random
import art

cards = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
         "J": 10, "Q": 10, "K": 10}


def get_card():
    """Returns a random card from the deck."""
    return random.choice(list(cards.keys()))


def calculate_cards(user_cards):
    """Take a list of cards and return the score calculated from the cards."""
    sum = 0
    for card in user_cards:
        if card == "A" and len(user_cards) == 2 and sum <= 10:
            sum += 11
        elif card == "A" and (sum > 10):
            sum += 1
        else:
            card = int(cards[card]) #Returns the value of the actual key card from the dictionary k = 10
            sum += card
            if sum > 21:
                return sum
    return sum


def blackjack():
    print(art.logo)

    player_cards = []
    dealer_cards = []

    for _ in range(2):
        player_cards.append(get_card())
        dealer_cards.append(get_card())

    player_score = calculate_cards(player_cards)
    dealer_score = calculate_cards(dealer_cards)

    print(f"Your cards: {player_cards}, Your current score: {player_score}")
    print(f"Dealer card: ['{dealer_cards[0]}']")

    extra = input("Type \"y\" to get an another card, type \"n\" to pass: ").lower()
    while extra == "y":
        player_cards.append(get_card())
        player_score = calculate_cards(player_cards)
        if player_score > 20:
            extra = "n"
        else:
            print(f"Your cards: {player_cards}, Your current score: {player_score}")
            extra = input("Type \"y\" to get an another card, type \"n\" to pass: ").lower()

    while dealer_score < 17:
        dealer_cards.append(get_card())
        dealer_score = calculate_cards(dealer_cards)

    print(f"\n" * 20)
    print(f"Your cards {player_cards}")
    print(f"Dealer cards {dealer_cards}")

    print(f"{player_score} X {dealer_score}", end=" ")

    if player_score == dealer_score:
        if (len(player_cards) == 2 and player_score == 21) and len(dealer_cards) > 2:
            print("You won with a Blackjack!!!")
        else:
            print("Draw!")
    elif dealer_score > 20 and len(dealer_cards) == 2:
        print("You lose! Dealer won with a Blackjack!")
    elif player_score > 20 and len(player_cards) == 2:
        print("You won with a Blackjack!!!")
    elif player_score > 21:
        print("You went over. You lose!")
    elif dealer_score > 21:
        print("Dealer went over. You win!")
    elif player_score > dealer_score:
        print("You won!")
    else:
        print("You lose!")

while input("\nDo you want to play a game of Blackjack? Type \"y\" or \"n\": ").lower() == "y":
    print("\n" * 20)
    blackjack()
