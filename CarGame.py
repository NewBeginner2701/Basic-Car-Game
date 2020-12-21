import pygame   # import pygame package
pygame.init()   # initiate package

grey = (118, 119 , 110)     # colour code in RGB form
black = (0,0,0)
display = pygame.display.set_mode((1000,600))   # set width & height of display
pygame.display.set_caption("Rutvik KA Gadi Hai")    # set window name
carimg = pygame.image.load("car1.png")      # load car image
backgroundleft = pygame.image.load("left.png")  # load background left side image
backgroundright = pygame.image.load("right.png")    # load background right side image 
car_width = 23

import time     # import the time for restart the game 
import random   # import for random position police car comes

def policecar(police_startx, police_starty, police):    # define the police function
    if police == 0 :    # at 0 stage 
        police_come = pygame.image.load("car2.png") # police car2 come

    if police == 1:     # at 1 stage
        police_come = pygame.image.load("car3.png") # police car3 come

    if police == 2:
        police_come = pygame.image.load("car1.png") # police car1 come

    display.blit(police_come, (police_startx, police_starty))   # display the police car

def crash():    # create crash function to display this message
    message_display("CAR CRASHED")  # display this message call the message_display function

def message_display(text):   # create a function for message edit
    largetext = pygame.font.Font("freesansbold.ttf", 60)    # message in this style and size will be 80
    textsurf,textrect = text_object(text, largetext)   # create function to edit message
    textrect.center = ((400), (200))  # show the message position in display
    display.blit(textsurf,textrect)     # display this message 
    pygame.display.update()     # update display
    time.sleep(2)   # after crashed 2 sec restart the game
    loop()      # call the loop function to restart the game 

def text_object(text, font):    # display after crash the car
    textsurface = font.render(text, True, black)    # display in this colour 
    return textsurface, textsurface.get_rect()      # after that restart the game & ready to give some input

def background():
    display.blit(backgroundleft, (0,0))     # set left side position of background image at x-axis & y-axis
    display.blit(backgroundright, (700, 0))     # set right position of background image at x-axis & y-axis

def car(x,y):   # create car function
    display.blit(carimg, (x,y))     # set position of car

def loop():     # all the function are called using this function
    x = 400     # x axis position for car
    y = 540     # y axis position for car
    x_change = 0    # set x position at x-axis 
    y_change = 0    # set y position at y-axis
    policecar_speed = 5     # police car speed
    police = 0  # police car in 0 stage
    police_startx = random.randrange(130, (700-car_width))      # police car in x-axis comes randomly 
    police_starty = -600    # police car comes in y-axis -600 because opposite side
    police_width = 23       # police car width 
    police_height = 47      # police car height 

    bumped = False  # if game is not any problem to start
    while not bumped:   # game is start
        for event in pygame.event.get():    # if any input is given
            if event.type == pygame.QUIT:   # if quit input is given
               # bumped = True   # game is stop
               pygame.quit()
               quit()
            
            if event.type == pygame.KEYDOWN:        # if any key pressed
                if event.key == pygame.K_LEFT:      # if pressed key is left
                    x_change = -5   # move left side by -5

                if event.key == pygame.K_RIGHT:     # if pressed key is right 
                    x_change = +5   # move right side by +5

            if event.type == pygame.KEYUP:  # if key is unpressed then
                x_change = 0

        x+=x_change 

        display.fill(grey)  # apply colour to display
        background()
        police_starty-=(policecar_speed/4)    # police car speed at y-axis 
        policecar(police_startx, police_starty, police)     # call police function
        police_starty+=policecar_speed    # police car speed increase 
        car(x,y)    # call the function of car
        if x < 130 or x > 700-car_width:    # if car goes out of this range
            # bumped = True     # gamw is stop
            crash()     # call crash function
        
        if police_starty > 600:     # police car pass it without crashed
            police_starty = 0-police_height     # only one is croosed 
            police_startx = random.randrange(130, (1000-300))   # another car is come
            police = random.randrange(0,2)  # different car come

        if y < police_starty + police_height:  # if police car is not pass
            if x > police_startx and x < police_startx + police_width or x + car_width > police_startx and x + car_width < police_startx + police_width :
                crash() # crash the car

        pygame.display.update()     # update the display 
loop()  # call the loop function
pygame.quit()   # package is stop
quit()      # game is stop