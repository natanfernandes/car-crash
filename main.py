import pygame
pygame.init()

windowW = 1000
windowH = 600
clock = pygame.time.Clock()
window = pygame.display.set_mode((windowW,windowH))
pygame.display.set_caption("Car crash")

class Car(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.crashCount = 0
        self.left = False
        self.right = False
        self.bottom = False

# start at bottom middle of window
x = windowH-100
y = windowW/2

# images of cars curve
curveRight = pygame.image.load('r3.png')
curveLeft = pygame.image.load('l3.png')
curveBottom = pygame.image.load('b3.png')
carNormal = pygame.image.load("car.png")

width = 64
height = 64
vel = 20
game = True

left = False
right = False
bottom = False

def create_car(img):
    car_surface = pygame.Surface((64,64))  
    car_surface.set_alpha(0)  
    car_surface.fill((255,255,255))
    window.blit(car_surface, (x,y))
    window.blit(img, (x,y))


def create_trash():
    trash = pygame.image.load("trash.png")
    trash_surface = pygame.Surface((64,64))  
    trash_surface.set_alpha(0)  
    trash_surface.fill((255,255,255))
    window.blit(trash_surface, (100,100))
    window.blit(trash, (100,100))

def create_bg():
    bg = pygame.image.load("bg.png")
    window.blit(bg, (0, 0))

    if left:
        create_car(curveLeft)
    elif right:
        create_car(curveRight)
    elif bottom:
        create_car(curveBottom)
    else:
        create_car(carNormal)
    pygame.display.update()

while game:
    clock.tick(9)

    #detect events in game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel:
        x = x-vel
        left = True
        right = False
        bottom = False
       
        print(x)

    if keys[pygame.K_RIGHT] and x < (windowW-width):
        x = x+vel
        left = False
        right = True
        bottom = False
        
        print(x)

    if keys[pygame.K_UP] and y > 0:
        y = y-vel
        left = False
        right = False
        bottom = False
        
        print(y)

    if keys[pygame.K_DOWN] and y < (windowH-height-20):
        y= y+vel
        left = False
        right = False
        bottom = True
        

    create_bg()



pygame.quit()