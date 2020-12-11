import pygame
import os
import datetime as dt
from time import sleep
import math

'''
This is the mock version of the main application
Just something like a wireframe
No camera and ultrasonic are being used here
'''

#-----------------Const---------------------

red = (200,0,0)
lightred = (255,0,0)
green = (0,200,0)
lightgreen = (0,255,0)
blue = (0,0,200)
lightblue = (0,0,255)
orange = (255,153,51)
lightorange = (255,178,102)
white = (255,255,255)
grey = (224,224,224)
dgrey = (200,200,200)
black = (0,0,0)
X = 800
Y = 480
admin = ['Jay', 'Prime']
img_path = './pic/faces'
clock = pygame.time.Clock()

#----------------Let-----------------------

guest_no = 1
weight = "20"

#---------------Setup----------------------

pygame.init()
screen = pygame.display.set_mode((X,Y))
pygame.display.set_caption("Candy Dispenser")

# while True:
#     img_path = img_path+'/others/capture{}.jpg'.format(str(guest_no))
#     if(not os.path.exists(img_path)):
#         break
#     guest_no += 1

#------------Components--------------------

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def text(des,font,size,posx,posy,color=black):
    largeText = pygame.font.SysFont(font,size)
    TextSurf, TextRect = text_objects(des, largeText, color)
    TextRect.center = (posx,posy)
    screen.blit(TextSurf, TextRect)

def picture(name,posx,posy,alpha):
    bg = pygame.image.load(name).convert()
    bgrect = bg.get_rect()
    bgrect.center = (posx,posy)
    bg.set_alpha(alpha)   
    screen.blit(bg,bgrect)

def numpad(weight_input):
    np = [Button(str(i),60,60,grey,dgrey,20) for i in range (10)]
    
    delete = Button("DEL",60,60,grey,dgrey,20)
    clear = Button("CLR",60,60,grey,dgrey,20)
    
    np[1].place(X/9,Y/2-45)
    np[2].place(X/9+70,Y/2-45)
    np[3].place(X/9+140,Y/2-45)
    np[4].place(X/9,Y/2+25)
    np[5].place(X/9+70,Y/2+25)
    np[6].place(X/9+140,Y/2+25)
    np[7].place(X/9,Y/2+95)
    np[8].place(X/9+70,Y/2+95)
    np[9].place(X/9+140,Y/2+95)
    np[0].place(X/9+70,Y/2+165)
    delete.place(X/9+140,Y/2+165)
    clear.place(X/9,Y/2+165)

    if(len(weight_input)<6):
        for i in range (10): 
            if(np[i].is_clicked()):
                if((not len(weight_input)==0 ) or (not np[i].msg=="0")):
                    weight_input.append(i)
    
    if(delete.is_clicked()):
        if(len(weight_input)!=0):
            weight_input.pop()
             
    if(clear.is_clicked()):
        weight_input.clear()

class Button(object):
    def __init__(self,msg,w,h,ic,ac,msgz,msgc=black):
        self.msg = msg
        self.w = w
        self.h = h
        self.ic = ic
        self.ac = ac
        self.msgz = msgz
        self.msgc = msgc
    
    def place(self,x,y):
        self.x = x
        self.y = y
        mouse = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()
        if(x+self.w > mouse[0] > x and y+self.h > mouse[1] > y):
            pygame.draw.rect(screen, self.ac, (x,y,self.w,self.h))  #posx,posy,dimx,dimy
        
        else:
            pygame.draw.rect(screen, self.ic, (x,y,self.w,self.h))
        
        btnText2 = text(self.msg,"Quicksand Medium",self.msgz,x+self.w/2,y+self.h/2,self.msgc)

    def is_clicked(self):
        mouse = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()

        if(self.x+self.w > mouse[0] > self.x and self.y+self.h > mouse[1] > self.y):
            if(clicked[0] == 1):
                sleep(0.3)
                return True
        
        return False

#--------------Pages-----------------

def main_menu():
    boundary = -X/4
    alpha = 0
    is_inserted = 0
    run = True
    while run:

        for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
            if event.type == pygame.QUIT: # Checks if the red button in the corner of the window is clicked
                run = False  # Ends the game loop
    
        screen.fill(white)
        
        doge = picture('pic/assets/doge2.jpg',X/4+40,Y/2,alpha)
        if(alpha<128):
            alpha += 3
        
        title = text("IoT Candy Dispenser","Quicksand",40,boundary,60)
        if(boundary<X/4+45):
            boundary += 9
        
        bclose = Button("",40,40,white,white,20)
        bclose.place(X*3/4+120,Y/4-90)
        cross = picture('pic/assets/cross.jpg',X*3/4+140,Y/4-70,255)

        if bclose.is_clicked() :
            run = False
        
        candyBtn = Button("Candy",100,50,orange,lightorange,20)
        candyBtn.place(X-200,Y/2+20)
        # swipe = text("Swipe the sensor to proceed","Quicksand",20,X-150,Y/2+50)

        settingBtn = Button("",40,40,grey,black,20)
        settingBtn.place(X*3/4+120,Y-80)
        gear = picture('pic/assets/setting2.jpg',X*3/4+140,Y-60,255)
                  
        if(candyBtn.is_clicked()):
            candy_detect_page()
            boundary = -X/4
            alpha = 0

        if(settingBtn.is_clicked()):
            admin_password()
            boundary = -X/4
            alpha = 0

        pygame.display.update() 
        clock.tick(30)

def candy_detect_page():
    run = True
    
    while run:

        for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
            if event.type == pygame.QUIT: # Checks if the red button in the corner of the window is clicked
                run = False  # Ends the game loop
    
        screen.fill(white)
        
        status = text("Opening the camera...","Quicksand",35,X/2,45)

        cardBtn = Button("Detect",100,50,orange,lightorange,20)
        cardBtn.place(X/2-50,Y/2)

        cardBtn2 = Button("Detect2",100,50,orange,lightorange,20)
        cardBtn2.place(X/2-50,Y/2+80)

        if(cardBtn.is_clicked()): 
            candy_complete('Jay')
            run = False

        if(cardBtn2.is_clicked()):
            candy_fail()  
            run = False 

        pygame.display.update() 
        clock.tick(30)

def candy_complete(person):
    run = True
    count = 5

    while run:

        for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
            if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN: # Checks if the red button in the corner of the window is clicked
                run = False  # Ends the game loop
    
        screen.fill(white)
        
        if(count == 1):
            run = False

        status = text("Registration complete","Quicksand",35,X/2,45)

        info = text("Enjoy your candy!","Quicksand",40,X/2,Y/2)
        
        leave = text("Back to main menu in ","Quicksand",20,(X/2),Y-80)

        countdown = text(str(count),"Quicksand",20,2*X/3-20,Y-80)

        pygame.display.update()
        
        count -= 1

        clock.tick(1)  

def candy_fail():
    run = True
    count = 5

    while run:

        for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
            if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN: # Checks if the red button in the corner of the window is clicked
                run = False  # Ends the game loop
    
        screen.fill(white)
        
        if(count == 1):
            run = False
        
        status = text("You already take candy la!","Quicksand",40,X/2,Y/2)
            
        leave = text("Back to main menu in ","Quicksand",20,(X/2),Y-80)

        countdown = text(str(count),"Quicksand",20,2*X/3-20,Y-80)

        pygame.display.update()
        
        count -= 1

        clock.tick(1)  

def admin_password():
    run = True
    while run:

        for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
            if event.type == pygame.QUIT: # Checks if the red button in the corner of the window is clicked
                run = False  # Ends the game loop
    
        screen.fill(white)
        
        status = text("Please authorize as admin before proceed","Quicksand",35,X/2,45)
        status2 = text("Opening the camera...","Quicksand",35,X/2,90)

        cardBtn = Button("Detect",100,50,orange,lightorange,20)
        cardBtn.place(X/2-50,Y/2)

        cardBtn2 = Button("Detect2",100,50,orange,lightorange,20)
        cardBtn2.place(X/2-50,Y/2+70)
        
        if(cardBtn.is_clicked()):
            admin_setting('Jay')
            run = False
        
        if(cardBtn2.is_clicked()):
            admin_wrong_password()
            run = False

        pygame.display.update() 
        clock.tick(30)

def admin_setting(name):
    run = True
    weight_input = []
    global weight

    while run:

        for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
            if event.type == pygame.QUIT: # Checks if the red button in the corner of the window is clicked
                run = False  # Ends the game loop

        slide = 0
        screen.fill(white)
        
        status = text("Hi {}!".format(name),"Quicksand",35,X/2,45)

        info = text('Input the new amount of weight',"Quicksand",25,3*X/4,Y/3-10)
        
        current_weight = text("Current weight: {} grams".format(weight),"Quicksand",20,X/4,Y/4-30)
        pygame.draw.rect(screen,grey,(50,Y/4,300,50))
         
        for num in weight_input:
            text(str(num),"Quicksand",25,150+slide,Y/4+25)
            slide += 15

        removeBtn = Button("Remove guest",210,50,orange,lightorange,20)
        removeBtn.place(2*X/3,Y/2)

        cardBtn = Button("Save",100,50,orange,lightorange,20)
        cardBtn.place(2*X/3,Y-100)
        
        if(cardBtn.is_clicked()):
            if(len(weight_input)!=0):
                weight = ""
            for num in weight_input:
                weight += str(num)
            print(weight)
            run = False
        
        np = numpad(weight_input)

        pygame.display.update() 
        clock.tick(30)

def admin_wrong_password():
    run = True
    blink = 0

    while run:

        for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
            if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN: # Checks if the red button in the corner of the window is clicked
                run = False  # Ends the game loop
    
        screen.fill(white)
        
        
        status = text("You are not authorized!","Quicksand",40,X/2,Y/2)
            
        if(blink<30): 
            leave = text("-Touch to leave-","Quicksand",20,(X/2),Y-80)
        if(blink>60):
            blink = 0   
        blink += 1

        pygame.display.update() 
        clock.tick(30)


main_menu()

pygame.quit()  # If we exit the loop this will execute and close our game
