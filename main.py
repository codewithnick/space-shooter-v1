from obstacles import *
from random import *
from time import *
import pygame
pygame.init()
white = (255, 255, 255)
GREY= (198, 198, 198)
black= (0,0,0)
# assigning values to height and width variable   
height = 600  
width = 600
#global variables
backgroundx=-806
backgroundy=-806
sizecarx=99
sizecary=75
carx=(height-sizecarx)//2
cary=width-sizecary
carxrange=list(i for i in range(carx,carx+sizecarx))
fps=10
i=1
# creating the display surface object
# of specific dimension..e(X, Y).   
display_surface = pygame.display.set_mode((height, width))
background=pygame.display.set_caption('Space Shooter')
background = pygame.image.load(r'png/background/image.png')  
car=[pygame.image.load(r'png/playerLeft.png'),pygame.image.load(r'png/player.png'),pygame.image.load(r'png/playerRight.png')]
########################################################bullet#################################################################
laser = pygame.image.load(r'png/laserGreen.png')
bulletx=carx+sizecarx//2 +40
bullety=cary+sizecary//2
bulletsizex=9
bulletsizey=33
bulletlist1=[]
bulletlist2=[]
bulletspeed=20
#bullet class
###################################################meteor##################################################################
bigmeteorsizex=136
bigmeteorsizey=111
smallmeteorsizex=44
smallmeteorsizey=42
smallmeteor = pygame.image.load(r'png/meteorSmall.png')
bigmeteor = pygame.image.load(r'png/meteorBig.png')
meteorshot = pygame.image.load(r'png/meteorshot.png').convert()
meteorshot.set_colorkey(white)
smallmeteorx=randint(0,height-smallmeteorsizex)
smallmeteory=randint(0,width-smallmeteorsizey)
small_meteor_obj=Meteor(smallmeteorx,smallmeteory)
bigmeteorx=randint(0,height-bigmeteorsizex)
bigmeteory=randint(0,width-bigmeteorsizey)
big_meteor_obj=Meteor(bigmeteorx,bigmeteory)
smallmeteorlist=[]
bigmeteorlist=[]
#playershot=Bullet(laser,display_surface,bulletx,bullety)
################################################################################enemy spaceship#############################################################
#maingameloop
count=0
while True:
    display_surface.fill(white)  
    display_surface.blit(background,(backgroundx, backgroundy))
    display_surface.blit(car[i],(carx, cary))
    keys = pygame.key.get_pressed()  #checking pressed keys
    for x in smallmeteorlist:
        if not x.meteorhits:
            display_surface.blit(smallmeteor,(x.meteorx,x.meteory))
        else:
            display_surface.blit(meteorshot,(x.meteorx,x.meteory))
        x.meteory+=fps
    for x in bigmeteorlist:
        if not x.meteorhits:
            display_surface.blit(bigmeteor,(x.meteorx,x.meteory))
        else:
            display_surface.blit(meteorshot,(x.meteorx,x.meteory))
        x.meteory+=fps
    for x in bulletlist1:
        display_surface.blit(laser,(x.bulletx,x.bullety))
        x.bullety-=bulletspeed
    for x in bulletlist2:
        display_surface.blit(laser,(x.bulletx,x.bullety))
        x.bullety-=bulletspeed
    for event in pygame.event.get():
        i=1
        if event.type == pygame.QUIT:  
            pygame.quit()  
            # quit the program.   
            quit()
        elif event.type == pygame.KEYDOWN:
            # Space bar! Spawn a new ball.
            if event.key == pygame.K_SPACE:
                playershot=Bullet(bulletx,bullety)
                bulletlist1.append(playershot)
                playershot=Bullet(bulletx-sizecarx+10,bullety)
                bulletlist2.append(playershot)
   
    if(backgroundy<0):
        backgroundy+=fps
    else:
        backgroundy=-806
    if backgroundx>0 or backgroundx<-806:
        backgroundx=-806
    if keys[pygame.K_UP]:
        backgroundy += fps
    if keys[pygame.K_DOWN]:
        backgroundy -= fps

    if keys[pygame.K_LEFT]:
        i=0
        backgroundx += fps
        for x in smallmeteorlist:
            x.meteorx+=fps
        for x in bigmeteorlist:
            x.meteorx+=fps
    if keys[pygame.K_RIGHT]:
        i=2
        backgroundx -= fps
        for x in smallmeteorlist:
            x.meteorx-=fps
        for x in bigmeteorlist:
            x.meteorx-=fps
##    if keys[pygame.K_SPACE]:
##        playershot=Bullet(bulletx,bullety)
##        bulletlist.append(playershot)
##
    for x in bulletlist1:
        if x.bullety<0:
            bulletlist1.remove(x)
    if len(bulletlist1)>3:
        bulletlist1.pop(len(bulletlist1)-1)
    for x in bulletlist2:
        if x.bullety<0:
            bulletlist2.remove(x)
    if len(bulletlist2)>3:
        bulletlist2.pop(len(bulletlist2)-1)
    if len(smallmeteorlist)>3:
        smallmeteorlist.pop(0)
    #playershot.bullety-=1
    #playershot=Bullet(laser,display_surface,bulletx,playershot.bullety)
    if count%30==0:
        ################making meteors####################
        smallmeteorx=randint(0,height-smallmeteorsizex)
        small_meteor_obj=Meteor(smallmeteorx,0)
        smallmeteorlist.append(small_meteor_obj)
    if count==100:
        count=0################making meteors####################
        bigmeteorx=randint(0,height-bigmeteorsizex)
        big_meteor_obj=Meteor(bigmeteorx,0)
        bigmeteorlist.append(big_meteor_obj)
    
    ############################# meteor hits #########################
    for x in smallmeteorlist:
        if x.meteory>=cary and (x.meteorx in carxrange or x.meteorx+smallmeteorsizex in carxrange):
            x.meteorhits=True
            pass
    for x in bigmeteorlist:
        if x.meteory+(bigmeteorsizey)//2>=cary and (x.meteorx in carxrange or x.meteorx+bigmeteorsizex in carxrange or x.meteorx+(bigmeteorsizex)//2 in carxrange):
            x.meteorhits=True
            pass    
    for a in bulletlist1:
        for x in bigmeteorlist:
            if a.bullety<=x.meteory and (a.bulletx in x.bigmeteorrange or a.bulletx+bulletsizex in x.bigmeteorrange):
                x.meteorhits=True
        for x in smallmeteorlist:
            if a.bullety<=x.meteory and (a.bulletx in x.smallmeteorrange or a.bulletx+bulletsizex in x.smallmeteorrange):
                x.meteorhits=True
    for a in bulletlist2:
        for x in bigmeteorlist:
            if a.bullety<=x.meteory and (a.bulletx in x.bigmeteorrange or a.bulletx+bulletsizex in x.bigmeteorrange):
                x.meteorhits=True
        for x in smallmeteorlist:
            if a.bullety<=x.meteory and (a.bulletx in x.smallmeteorrange or a.bulletx+bulletsizex in x.smallmeteorrange):
                x.meteorhits=True
        
    count+=1
    pygame.display.update()
    
