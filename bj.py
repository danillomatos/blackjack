from random import shuffle
from IPython.display import clear_output

class Hand():
    def __init__(self, identifier, deck_list):
        
        self.identifier = identifier
        self.deck_list = deck_list
        self.card_number, self.suit_symbol = self.deck_list[self.identifier]
    def __str__(self):
        if self.card_number != 10:
            return f"____\n|{self.card_number}  |\n| {self.suit_symbol} |\n|__{self.card_number}|"
        else:
            return f"\r____\n|{self.card_number} |\n| {self.suit_symbol} |\n|_{self.card_number}|"
    def card_value(self):
        try:
            if 2 <= self.card_number <= 10:
                return self.card_number
        except:
            if self.card_number in ('J', 'Q', 'K'):
                return 10
            else:
                return 11
    
class Player():
    def _init__(self, name, balance):
        self.name = name
        self.balance = balance

def blackjack_sum(thecards):
    player_card_values = [numbers.card_value() for numbers in thecards]
    player_card_sum = sum(player_card_values)
    for p in range(0,player_card_values.count(11)):
        if player_card_sum>21:
            player_card_sum -= 10
    return player_card_sum

def start_game(player_name, player_cash):
    card_list = ['A'] + list(range(2,11)) +  ['J', 'Q', 'K']
    suit_list = ['♠', '♥', '♣', '♦']
    deck_list = [ ]
    idx = 0
    for c in card_list:
        for s in suit_list:
            deck_list.append((c,s))
            idx += 1
    shuffle(deck_list)
    
    player_action = 'start'
    index = len(player_name)*2
    your_cards = [Hand(index-2,deck_list), Hand(index-1,deck_list)]
    dealer_cards = [Hand(index,deck_list)]

    while True:
        try:
            bet_money = float(input("Place your bet: "))
            if bet_money > player_cash:
                print("Insufficient funds, try a different value!")
                continue
            if bet_money == 0:
                print("If you bet nothing, you win nothing, and what's the point?? Try again!")
                continue
        except:
            print('\nUse actual numbers to place bet!')
        else:
            break
    

    while player_action != 'won' and player_action != 'lost':
        player_card_sum = blackjack_sum(your_cards)
        dealer_card_sum = blackjack_sum(dealer_cards)
        clear_output()
        print(f"\nThe dealer has: {dealer_card_sum}")

        for i in dealer_cards:
            print(i)
        print(f"\nYou have: {player_card_sum}")

        for m in your_cards:
            print(m)
        
        if player_card_sum > 21:
            player_action = 'lost'
            print('\nHA! YOU BUSTED :P')
            player_cash -= bet_money
            break
        elif player_card_sum == 21:
            player_cash += bet_money
            player_action = 'won'
            print('\nBlackjack! You won!')
            break
        
        while True:
            player_action = input("Would you like to hit or stand? ").lower()
            if player_action !='hit' and player_action!='stand':
                print("\nThere are only two options you piece of shit!")
            else:
                break
        if player_action == 'hit':
            index += 1
            your_cards += [Hand(index,deck_list)]
        else:
            while dealer_card_sum <= player_card_sum:
                index += 1
                dealer_cards += [Hand(index,deck_list)]
                dealer_card_sum = blackjack_sum(dealer_cards)
                clear_output()
                print(f"\nThe dealer has: {dealer_card_sum}")

                for i in dealer_cards:
                    print(i)
                print(f"\nYou have: {player_card_sum}")

                for m in your_cards:
                    print(m)
                
                if  dealer_card_sum > player_card_sum and dealer_card_sum<=21:
                    player_action = 'lost'
                    player_cash -= bet_money
                    print("\nThe house always wins!")

                elif dealer_card_sum > 21:
                    print("\nYou won!")
                    player_cash += bet_money
                    player_action = 'won'
    print(f"\nThanks for the ride, {player_name}! You now got ${player_cash} in the bank!")
    return player_cash

while True:
    wannaplay = input("\nWhat's up? Wanna play some cool stuff? [yes or no] ").lower()
    if wannaplay != 'yes' and wannaplay != 'no':
        print("\nThat's illegal af. Try again!")
    else:
        break

if wannaplay == 'no':
    print ('\nWell then, see you next time!')
else:
    player_name = input('Please enter your name: ')
    while True:
        try:
            player_cash = float(input('Enter deposit amount: '))
        except:
            print('\nYou are not speaking money language here!')
        else:
            break
            
    player_cash = start_game(player_name,player_cash)
    while True:
        replay_answer = input("\nWould you like to play another hand? [yes or no] ").lower()
        if replay_answer == 'yes':
            clear_output()
            if player_cash == 0:
                print( "\nYou are out of money. Go home, punk!")
                break
            player_cash = start_game(player_name,player_cash)
        elif replay_answer == 'no':
            print(f"\nAlright, {player_name}. Goodbye!")
            break
        else:
            print( "\nIllegal answer, try again!")
