import pygame
from pygame.locals import *
import random
import time
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Shapes!!")
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
black = (0,0,0)
white = (255,255,255)
gold = (245,230,0)
colors = [red,green,blue,yellow,gold]
balloon1 = pygame.image.load('balloon.png')
balloon1 = pygame.transform.scale(balloon1,(80,80))
balloons = []
clock = pygame.time.Clock()
over = False
def show_text(msg,x,y,color,size):
        fontobj= pygame.font.SysFont('freesans',size)
        msgobj = fontobj.render(msg,False,color)
        screen.blit(msgobj,(x,y))
class balloon():
    def __init__(self,x,y,image,letter):
        self.x = x
        self.y = y
        self.image = image
        self.letter = letter

    def draw(self):
        screen.blit(self.image,(self.x,self.y))
        show_text(self.letter,self.x+50,self.y-5,white,32)
    def move(self):
        self.y += 1
    def game(self):
        global over
        if self.y == 600:
            show_text("Game Over",300,300,red,60)
            over = True;



for a in range(1,11,1):
    randx = random.randint(0,600)
    randy = random.randint(0,150)
    randa = random.randint(97,122)
    newballoon = balloon(randx,randy,balloon1,chr(randa))
    balloons.append(newballoon)

while True:
    
    if over == True:
        pygame.display.update()
        break
    
    for a in balloons:
        a.draw();
        a.move()
        a.game()
    pygame.display.update()
    screen.fill(black)
    clock.tick(80)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit();
        if event.type == pygame.KEYDOWN:
            for a in balloons:
                if chr(event.key) == a.letter:
                    balloons.remove(a)
            


    

        
    
