# Rock-paper-scissors-lizard-Spock
#Name : Noor Muhammad

# Run this code in http://codeskulptor.org for better performance using google chrome or firefox brower

import simplegui

time = 0
tens_sec = 0
successful_stop = 0
total_stop = 0


# define global variables


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global tens_sec
    if t < 600:
        min = 0
        tens_sec = t % 10
        t = t / 10
        sec = t
        
        if sec < 10:
            sec = "0" + str(sec)
    elif t > 600:
        min = t / 600
        sec = t % 600
        tens_sec = sec % 10
        sec = sec / 10
        
        if sec < 10:
            sec = "0" + str(sec)
    else:
        min = 1
        sec = "00"
        tens_sec = 0
        
    return str(min) + ":" + str(sec) + "." + str(tens_sec)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button():
    timer.start()
    
def stop_button():
    global total_stop,successful_stop, tens_sec
    timer.stop()
    total_stop += 1
    if tens_sec == 0:
        successful_stop += 1
    
def reset_button():
    global time, total_stop, successful_stop
    time = 0
    total_stop = 0
    successful_stop = 0
    timer.stop()

# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time += 1

# define draw handler
def draw(canvas):
    global total_stop,successful_stop
    canvas.draw_text(format(time),[120,100],32,"white")
    canvas.draw_text((str(successful_stop)+"/"+str(total_stop))
                     ,[255,30],24,"green")
                     

    
# create frame
frame = simplegui.create_frame("Mini Project", 300,200)


# register event handlers
frame.set_draw_handler(draw)

timer = simplegui.create_timer(100,tick)

frame.add_button("Start",start_button,150)
frame.add_button("Stop",stop_button,150)
frame.add_button("Reset",reset_button,150)


# start frame
frame.start()
