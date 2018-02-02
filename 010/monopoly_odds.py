import random

from itertools import chain, repeat
from namedlist import namedlist
from collections import OrderedDict

BOARD_SQUARES = "GO A1 CC1 A2 T1 R1 B1 CH1 B2 B3 JAIL C1 U1 C2 C3 R2 D1 CC2 D2 \
                        D3 FP E1 CH2 E2 E3 R3 F1 F2 U2 F3 G2J G1 G2 CC3 G3 R4 CH3 H1 T2 H2"

# set up card decks
COMMUNITY_CHEST = list(chain.from_iterable([list(repeat(v[0],v[1])) for v in \
                        (("GO", 1), ("JAIL", 1), ("NOTHING", 14))]))

CHANCE_DECK = list(chain.from_iterable([list(repeat(v[0],v[1])) for v in \
                        (("GO", 1), ("JAIL", 1), ("C1", 1), ("E3", 1), \
                        ("H2", 1), ("R1", 1), ("NEXTR", 1), ("NEXTU", 1), \
                        ("BACK3", 1), ("NOTHING", 14))]))

# shuffle decks (don't really have to do this)
random.shuffle(COMMUNITY_CHEST)
random.shuffle(CHANCE_DECK)    

# set up monopoly board
SQUARE = namedlist('square', 'name landed_on')
BOARD = OrderedDict((i,SQUARE(s, 0)) for i,s in enumerate(BOARD_SQUARES.split()))

class Player(object):
    def __init__(self):
        self._position = 0
        self._double_count = 0
    
    def roll_dice(self, sides):
        d1 = random.randrange(1,sides+1)
        d2 = random.randrange(1,sides+1)

        self.check_double(d1,d2)
        
        return self.move(d1 + d2)

    def check_double(self, d1, d2):
        if d1 == d2:
            self._double_count += 1
        else:
            self._double_count = 0

    def move(self, roll):
        self._position = (self._position + roll) % len(BOARD)       

        # if the square is special do something
        if BOARD[self._position].name == "G2J" or self._double_count >= 3:
            self._position = 10
            BOARD[self._position].landed_on += 1
            return
        elif BOARD[self._position].name[:2] == "CH":
            return self.pick_up_card(CHANCE_DECK)
        elif BOARD[self._position].name[:2] == "CC":
            return self.pick_up_card(COMMUNITY_CHEST)

        BOARD[self._position].landed_on += 1

    # go to square from picked up card
    def go_to_square(self, square):
        self._position = square
        BOARD[self._position].landed_on += 1

    # go to next train or utilities square
    def go_to_next(self, square_type):
        while square_type not in BOARD[self._position].name:
            self._position = (self._position + 1) % len(BOARD)
        BOARD[self._position].landed_on += 1

    def go_back_3(self):
        self._position -= 3
        BOARD[self._position].landed_on += 1

    # pick up community chest or chance card
    def pick_up_card(self, deck):
        card = deck.pop(0)
        deck.append(card) 
        if card[:4] == "NEXT":
            return self.go_to_next(card[4:])
        elif card[:4] == "BACK":
            return self.go_back_3() 
        else:
            for k,v in BOARD.items():
                if v.name == card:
                    return self.go_to_square(k)
                    break 
        BOARD[self._position].landed_on += 1     


def get_odds():
    player = Player() 

    rolls = 1000
    for i in range(rolls):
        player.roll_dice(6)

    square_percentages = OrderedDict((v.name,str(round((v.landed_on/rolls)*100,2))+"%") for k,v in BOARD.items())


    return square_percentages

if __name__ == '__main__':
    player = Player() 

    rolls = 1000
    for i in range(rolls):
        player.roll_dice(6)

    # print out square percentages
    for k,v in BOARD.items():
        print(v.name + str(k) +" : Landed on "+ str(round(v.landed_on / rolls * 100, 2)))


   