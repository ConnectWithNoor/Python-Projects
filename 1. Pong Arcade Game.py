# Implementation of classic arcade game Pong
# Noor Muhammad

# Run this code in http://codeskulptor.org for better performance using google chrome or firefox brower
# Date : 9th August, 2018

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2 
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left

def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2 , HEIGHT/2]
    ball_vel = [random.randrange(120, 240)/30,-random.randrange(60, 180)/30]
    
    if direction == RIGHT:
        ball_vel[0] = random.randrange(120,240)/30
    elif direction == LEFT:
        ball_vel[0] = -random.randrange(120,240)/30
    
    

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    
    paddle1_pos = (HEIGHT / 2) - HALF_PAD_HEIGHT
    paddle2_pos = (HEIGHT / 2) - HALF_PAD_HEIGHT
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0   
    
    spawn_ball(random.choice([RIGHT,LEFT]))

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # positional update of the ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2 , "red", "white")
    
    # ball collide with topcanvas.draw_line([HALF_PAD_WIDTH, paddle1_pos],
                  
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    # ball collide with bottom wall
    elif  ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    
    # update paddle's vertical position
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    
    # keep paddle on the screen
    if paddle1_pos < 0:
        paddle1_pos = 0
    elif paddle1_pos + PAD_HEIGHT > HEIGHT :
        paddle1_pos =  HEIGHT - PAD_HEIGHT
        
    if paddle2_pos < 0:
        paddle2_pos = 0
    elif paddle2_pos + PAD_HEIGHT > HEIGHT :
        paddle2_pos =  HEIGHT - PAD_HEIGHT
    
    # draw paddles (line 67 is Right Paddle, line 68 is left paddle)
    canvas.draw_line([WIDTH- HALF_PAD_WIDTH, paddle1_pos], [WIDTH - HALF_PAD_WIDTH, paddle1_pos+ PAD_HEIGHT], PAD_WIDTH, 'Red')
    canvas.draw_line([HALF_PAD_WIDTH,paddle2_pos],[HALF_PAD_WIDTH,paddle2_pos+ PAD_HEIGHT],PAD_WIDTH,"WHITE")
    
    
    # determine whether paddle and ball collide
    
    # For Left Paddle Collision (Paddle2)
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if paddle2_pos  <= ball_pos[1] <= paddle2_pos + PAD_HEIGHT and ball_pos[0] < WIDTH/2: 
            ball_pos[0] = BALL_RADIUS + PAD_WIDTH
            ball_vel[0] = - ball_vel[0]
            ball_vel[0] += ball_vel[0]*0.1 #10% speed increase
            ball_vel[1] += ball_vel[1]*0.1 ##10% speed increase
        else:
            score2 += 1
            spawn_ball(RIGHT)
            
    # For Right Paddle Collision (Paddle1)
    
    if ball_pos[0] >= (WIDTH - PAD_WIDTH) - BALL_RADIUS: 
        if paddle1_pos <= ball_pos[1] <= paddle1_pos + PAD_HEIGHT and ball_pos[0] > WIDTH/2: 
            ball_pos[0] = (WIDTH - PAD_WIDTH -1) - BALL_RADIUS
            ball_vel[0] = - ball_vel[0]
            ball_vel[0] += ball_vel[0]*0.1 #10% speed increase
            ball_vel[1] += ball_vel[1]*0.1 ##10% speed increase
        else:
            score1 += 1
            spawn_ball(LEFT)
            
    # draw scores
    canvas.draw_text(str(score2),[WIDTH - WIDTH/3.5, 50],50,"RED")
    canvas.draw_text(str(score1),[WIDTH/4, 50],50,"WHITE")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["w"]:
        paddle2_vel += -5
    elif key == simplegui.KEY_MAP["s"]:
        paddle2_vel += +5
        
    if key == simplegui.KEY_MAP["up"]:
        paddle1_vel += -5
    elif key == simplegui.KEY_MAP["down"]:
        paddle1_vel += +5
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle2_vel = 0
        
    if key == simplegui.KEY_MAP["up"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle1_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Reset Game",new_game,150)


# start frame
new_game()
frame.start()
