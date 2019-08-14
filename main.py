import pygame
import numpy as np  
pygame.init()

clock = pygame.time.Clock()

class Game(object):
    def __init__(self,width,height,title):
        self.window = pygame.display.set_mode((width,height))
        self.width = width
        self.height = height
        self.title = title
        self.caption = pygame.display.set_caption(title)

class Car(object):
    def __init__(self,x,y,width,height,velocity):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.crashCount = 0
        self.left = False
        self.right = False
        self.bottom = False
        self.vel = velocity

class Trash(object):
    def __init__(self,width,height):
        self.x = np.random.randint(game.width - 100)
        self.y = np.random.randint(game.height - 100)
        self.width = width
        self.height = height

# images of cars curve
curveRight = pygame.image.load('r3.png')
curveLeft = pygame.image.load('l3.png')
curveBottom = pygame.image.load('b3.png')
carNormal = pygame.image.load("car.png")

game = True

def create_car(img):
    car_surface = pygame.Surface((64,64))  
    car_surface.set_alpha(255)  
    car_surface.fill((255,255,255))

    game.window.blit(car_surface, (car.x,car.y))
    game.window.blit(img, (car.x,car.y))

def create_trash():
    trashImage = pygame.image.load("trash.png")

    trash_surface = pygame.Surface((64,64))  
    trash_surface.set_alpha(0)  
    trash_surface.fill((255,255,255))
    
    game.window.blit(trash_surface, (trash.x,trash.y))
    game.window.blit(trashImage, (trash.x,trash.y))
    pygame.display.update()

def create_bg():
    bg = pygame.image.load("bg.png")
    game.window.blit(bg, (0, 0))

    if car.left:
        create_car(curveLeft)
    elif car.right:
        create_car(curveRight)
    elif car.bottom:
        create_car(curveBottom)
    else:
        create_car(carNormal)
    pygame.display.update()

game = Game(1000,600,"Car crash")
car = Car((game.height-100),(game.width/2),64,64,20)
trash = Trash(64,64)

while game:
    clock.tick(9)

    #detect events in game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and car.x > car.vel:
        car.x = car.x - car.vel
        car.left = True
        car.right = False
        car.bottom = False
        
    if keys[pygame.K_RIGHT] and car.x < (game.width - car.width):
        car.x = car.x + car.vel
        car.left = False
        car.right = True
        car.bottom = False

    if keys[pygame.K_UP] and car.y > 0:
        car.y = car.y - car.vel
        car.left = False
        car.right = False
        car.bottom = False

    if keys[pygame.K_DOWN] and car.y < (game.height - car.height-20):
        car.y = car.y + car.vel
        car.left = False
        car.right = False
        car.bottom = True     

    create_bg()
    create_trash()


pygame.quit()