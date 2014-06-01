# Implementation of classic arcade game Pong

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
ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [0, 0]
paddle1_vel = 0
paddle2_vel = 0
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos[0] =  ball_pos = [WIDTH/2, HEIGHT/2]
    ball_vel[1] =-1 * random.randrange(3, 5)
    ball_vel[0] = random.randrange(3, 5)
    if direction == RIGHT:
        ball_vel[0] = ball_vel[0]
    else:
        ball_vel[0] = - ball_vel[0]
        

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos = HEIGHT/2
    paddle2_pos = HEIGHT/2
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    L_R =random.randrange(0, 2)
    if L_R == 0:
        spawn_ball(RIGHT)
    else:
        spawn_ball(LEFT)
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
    
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]  
    
    if (ball_pos[1] == BALL_RADIUS) or (ball_pos[1] == HEIGHT - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]
            
    elif ball_pos[0] <= PAD_WIDTH+BALL_RADIUS:
        if (ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT) and (ball_pos[1] <= paddle1_pos+HALF_PAD_HEIGHT):
            ball_vel[0] = -1.1 * ball_vel[0] 
        else:
            score2 += 1
            spawn_ball(RIGHT)
    elif ball_pos[0] >= WIDTH-PAD_WIDTH-BALL_RADIUS:
        if (ball_pos[1] >= paddle2_pos-HALF_PAD_HEIGHT) and (ball_pos[1] <= paddle2_pos+HALF_PAD_HEIGHT):
            ball_vel[0] = -1.1 * ball_vel[0] 
        else:
            score1 += 1
            spawn_ball(LEFT)              
            
    # draw ball
    canvas.draw_circle(ball_pos, 20, 3, 'White', 'White')
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    
    if (paddle1_pos <= HALF_PAD_HEIGHT) or (paddle1_pos >= HEIGHT - HALF_PAD_HEIGHT):
        paddle1_vel =0
   
    paddle2_pos += paddle2_vel
        
    if (paddle2_pos <= HALF_PAD_HEIGHT) or (paddle2_pos >= HEIGHT - HALF_PAD_HEIGHT):
        paddle2_vel = 0
    
          
    # draw paddles
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT], 
                     [HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], 
                     PAD_WIDTH, 'White')
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], 
                     [WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT], 
                     PAD_WIDTH, 'White')
    
    # draw scores
    canvas.draw_text(str(score1), (WIDTH/4, 40), 40, 'White')
    canvas.draw_text(str(score2), (WIDTH*3/4, 40), 40, 'White')   
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    if (key== simplegui.KEY_MAP["w"]) and (paddle1_pos > HALF_PAD_HEIGHT) :
        paddle1_vel = -5
    if (key == simplegui.KEY_MAP["s"]) and (paddle1_pos <= HEIGHT-HALF_PAD_HEIGHT):
        paddle1_vel = 5 
    if (key == simplegui.KEY_MAP["up"]) and (paddle2_pos > HALF_PAD_HEIGHT):
        paddle2_vel = -5
    if (key == simplegui.KEY_MAP["down"]) and (paddle2_pos < HEIGHT-HALF_PAD_HEIGHT):
        paddle2_vel = 5
    
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["w"]:
       paddle1_vel = 0
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0    
  

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart', new_game, 70)


# start frame
new_game()
frame.start()
