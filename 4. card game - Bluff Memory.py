# implementation of card game - Bluff Memory
#Name : Noor Muhammad

import simplegui
import random


# helper function to initialize globals
def new_game():
    global CARD_DECK, CARD_POS, CARD_EXPOSED, card_1, card_2, state, turn
    
    CARD_DECK = range(0,8) * 2
    random.shuffle(CARD_DECK)
    CARD_POS = [50, 70]
    CARD_EXPOSED = [False for i in range(len(CARD_DECK))]
    card_1 = 0
    card_2 = 0
    state = 0
    turn = 0
     
# define event handlers
def mouseclick(pos):
    global state, turn, card_1, card_2, CARD_EXPOSED
    # add game state logic here
    p = pos[0] // 50
    
    if CARD_EXPOSED[p] == False:
        if state == 0:
            state = 1 
            card_1 = p
            CARD_EXPOSED[card_1] = True
           
        elif state == 1:
            state = 2
            card_2 = p
            if card_1 != card_2:
                CARD_EXPOSED[card_2] = True
                turn += 1
               
        elif state == 2:
            if CARD_DECK[card_1] != CARD_DECK[card_2]:
                CARD_EXPOSED[card_1] = False
                CARD_EXPOSED[card_2] = False
                state = 0
                
            card_1 = p
            if CARD_EXPOSED[card_1] == False:
                CARD_EXPOSED[card_1] = True
                state = 1
                          
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global CARD_DECK
    for card in range(len(CARD_DECK)):
        if CARD_EXPOSED[card] == True:
            canvas.draw_text(str(CARD_DECK[card]), [CARD_POS[0] * card + 10, CARD_POS[1] ], 60, 'white')
        else:
            canvas.draw_polygon([(50 * card, 0), (50 * card + 50, 0),
                                 (50 * card + 50, 100), (50 * card, 100)], 2, 'Black', 'Green')
            
        label.set_text('Turns: ' + str(turn)) 


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric