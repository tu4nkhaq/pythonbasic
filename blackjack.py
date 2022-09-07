import random
from replit import clear
def deal_card():
    return random.choice([11,2,3,4,5,6,7,8,9,10,10,10,10])
user_card=[]
computer_card=[]
is_game_over=False
for _ in range(2):
    user_card.append(deal_card())
    computer_card.append(deal_card())

