import random 

# Initialize cards, types, and players intial amount of chips
card_categories = ['Hearts', 'Diamonds', 'Clubs', 'Spades'] 
cards_list = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'] 
deck = [(card, category) for category in card_categories for card in cards_list] 
player_chips = 100
player_score = 0
dealer_score = 0
bet = 0

# Shuffle the deck
random.shuffle(deck) 
player_card = [deck.pop(), deck.pop()] 
dealer_card = [deck.pop(), deck.pop()] 

# Function sets values for non-numerical cards
def card_value(card): 
    if card[0] in ['Jack', 'Queen', 'King']: 
        return 10
    elif card[0] == 'Ace': 
        return 11
    else: 
        return int(card[0]) 

def clear_list():
    global player_score
    global dealer_score
    player_score*=0
    dealer_score*=0

# Function checks score and prints the appropriate messages
def check_Score():
    global player_chips
    if player_score > 21: 
        print("Cards Dealer Has:", dealer_card) 
        print("Score Of The Dealer:", dealer_score) 
        print("Cards Player Has:", player_card) 
        print("Score Of The Player:", player_score) 
        print("Dealer wins (Player Loss Because Player Score is exceeding 21)")
        player_chips -= bet 
        clear_list()

    elif dealer_score > 21: 
        print("Cards Dealer Has:", dealer_card) 
        print("Score Of The Dealer:", dealer_score) 
        print("Cards Player Has:", player_card) 
        print("Score Of The Player:", player_score) 
        print("Player wins (Dealer Loss Because Dealer Score is exceeding 21)") 
        player_chips += bet
        clear_list()

    elif player_score > dealer_score: 
        print("Cards Dealer Has:", dealer_card) 
        print("Score Of The Dealer:", dealer_score) 
        print("Cards Player Has:", player_card) 
        print("Score Of The Player:", player_score) 
        print("Player wins (Player Has High Score than Dealer)") 
        player_chips += bet
        clear_list()

    elif dealer_score > player_score: 
        print("Cards Dealer Has:", dealer_card) 
        print("Score Of The Dealer:", dealer_score) 
        print("Cards Player Has:", player_card) 
        print("Score Of The Player:", player_score) 
        print("Dealer wins (Dealer Has High Score than Player)") 
        player_chips -= bet
        clear_list()

    else: 
        print("Cards Dealer Has:", dealer_card) 
        print("Score Of The Dealer:", dealer_score) 
        print("Cards Player Has:", player_card) 
        print("Score Of The Player:", player_score) 
        print("PUSH!")
        clear_list()

# Function prompts user to place a bet
def place_bet():
    print(f"You have {player_chips} chips.")
    bet = int(input("Place your bet: "))
    if bet > player_chips:
        print("You don't have enough chips!")

def main():
    while True:
        place_bet()
        global player_score
        global dealer_score
        # Prompt user for their next move
        while True: 
            player_score = sum(card_value(card) for card in player_card) 
            dealer_score = sum(card_value(card) for card in dealer_card) 
            print("Cards Player Has:", player_card) 
            print("Score Of The Player:", player_score) 
            print("\n") 
            choice = input('What do you want? ["hit" to request another card, "stop" to stop]: ').lower() 
            if choice == "hit": 
                new_card = deck.pop() 
                player_card.append(new_card) 
            elif choice == "stop": 
                break
            else: 
                print("Invalid choice. Please try again.") 
                continue
        # Add cards to dealer's hand
        while dealer_score < 17: 
            new_card = deck.pop() 
            dealer_card.append(new_card) 
            dealer_score += card_value(new_card) 
        
        print("Cards Dealer Has:", dealer_card) 
        print("Score Of The Dealer:", dealer_score) 
        print("\n") 

        check_Score()

if __name__ == "__main__":
    main()