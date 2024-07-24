import random
import os


def score_calculator(cards):
    if ([11, 10] in cards) and (len(cards) == 2):
        return 0
    if (11 in cards) and (sum(cards) > 21):
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def deal_cards():
    deck_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(deck_list)


def winning_conditions(player_score, computer_score):
    if player_score > 21 and computer_score > 21:
        return "You went over, you lose !"
    elif computer_score == player_score:
        return "Its a tie !"
    elif computer_score > 21:
        return "Opponent went over, you won !"
    elif computer_score == 0:
        return "Opponent has a blackjack, you lose!"
    elif player_score == 0:
        return "Winning with a blackjack !"
    elif player_score > computer_score:
        return "You win !"
    else:
        return "You lose !"


def play_game():
    game_status = input("Write 'Play' to start playing and type 'No' if you don't want to play: ").upper()
    while game_status in ["PLAY", "YES"]:
        os.system('cls')
        print(
            '''88          88                       88        88                       88         
    88          88                       88        ""                       88         
    88          88                       88                                 88         
    88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
    88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
    88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
    88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
    8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                                  ,88                                  
                                                888P"                                  '''
        )

        player_cards = []
        computer_cards = []
        is_game_over = False

        # Dealing 2 cards
        for i in range(2):
            player_cards.append(deal_cards())
            computer_cards.append(deal_cards())

        while not is_game_over:
            player_score = score_calculator(player_cards)
            computer_score = score_calculator(computer_cards)
            print(f"Your cards: {player_cards} with score of: {player_score}")
            print(f"One of the Computer's Cards: {computer_cards[random.randint(0, 1)]}")
            if (player_score == 0) or (computer_score == 0) or (player_score > 21):
                is_game_over = True
            else:
                draw_card_decision = input("Type 'y' to draw another card, type 'n' to pass: ").upper()
                if draw_card_decision == "Y":
                    player_cards.append(deal_cards())
                else:
                    is_game_over = True
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_cards())
            computer_score = score_calculator(computer_cards)
        print(f"    Your final hand: {player_cards}, Final score: {player_score}\n"
              f"    Computer's final hand: {computer_cards}, Final score: {computer_score}\n"
              f"    {winning_conditions(player_score, computer_score)}")

        game_status = input("Would you like to play again ?\n"
                            "type 'Play' or 'Yes' if yes, and 'No' if you dont want to play: ").upper()


play_game()
