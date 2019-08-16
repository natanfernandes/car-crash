import pygame
import numpy as np  
pygame.init()

clock = pygame.time.Clock()

def scrollY(screenSurf, offsetY):
    width, height = screenSurf.get_size()
    copySurf = screenSurf.copy()
    screenSurf.blit(copySurf, (0, offsetY))
    if offsetY < 0:
        screenSurf.blit(copySurf, (0, height + offsetY), (0, 0, width, -offsetY))
    else:
        screenSurf.blit(copySurf, (0, 0), (0, height - offsetY, width, offsetY))

class Game(object):
    def __init__(self,width,height,title):
        self.window = pygame.display.set_mode((width,height))
        self.width = width
        self.height = height
        self.title = title
        self.caption = pygame.display.set_caption(title)
        self.game_font = pygame.font.SysFont("Times New Roman", 25)
        self.player_lifes = 3
        self.bg = pygame.image.load("bg.png").convert_alpha()

    def start(self,move):
        self.window.blit(self.bg, (0, move))
        scrollY(self.bg, 20)
        batidas = self.game_font.render('Batidas:', 1, (255,0,0))
        qtd = self.game_font.render(str(car.crashCount), 1, (255,0,0))
        self.window.blit(batidas,(500,50))
        self.window.blit(qtd,(600,50))
        life_positions = [(50,50),(100,50),(150,50)]
        obstacles.create()

        for position in life_positions:
            game.window.blit(lifes,position)

        if car.left:
            car.create(curveLeft)
        elif car.right:
            car.create(curveRight)
        elif car.bottom:
            car.create(curveBottom)
        else:
            car.create(carNormal)

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
        self.hitbox = (self.x , self.y, self.width, self.height)
    
    def create(self,img):
        game.window.blit(img, (self.x,self.y))
        self.hitbox = (self.x , self.y, self.width, self.height)
        pygame.draw.rect(game.window,(255,0,0),self.hitbox,2)
        
    
    def hit(self):
        self.crashCount += 1
        print('bateu')

    def collide(self,obstacle):
        if (car.y - car.height/2) < (obstacle.hitbox[1] + obstacle.hitbox[3]/2) and (car.y -car.height/2) > (obstacle.hitbox[1] - obstacle.hitbox[3]/2):
            if(car.x + car.width/2) > (obstacle.hitbox[0]-obstacle.hitbox[2]/2) and (car.x + car.width/2) < (obstacle.hitbox[0]+obstacle.hitbox[2]/2):
                car.hit()
                return True
            elif(car.x-car.width/2) < (obstacle.hitbox[0]+obstacle.hitbox[2]/2) and (car.x + car.width/2) > (obstacle.hitbox[0]+obstacle.hitbox[2]/2):
                car.hit()
                return True
            else:
                return False
        elif ((car.y + car.height/2)< (obstacle.hitbox[1] + obstacle.hitbox[3]/2) and (car.y + car.height/2) > (obstacle.hitbox[1] - obstacle.hitbox[3]/2)):
            if(car.x + car.width/2) > (obstacle.hitbox[0]-obstacle.hitbox[2]/2) and (car.x + car.width/2) < (obstacle.hitbox[0]+obstacle.hitbox[2]/2):
                car.hit()
                return True
            elif(car.x-car.width/2) < (obstacle.hitbox[0]+obstacle.hitbox[2]/2) and (car.x + car.width/2) > (obstacle.hitbox[0]+obstacle.hitbox[2]/2):
                car.hit()
                return True
            else:
                return False
        else:
            return False
       

class Obstacles(object):
    def __init__(self):
        self.all = []
    
    def create(self):
        if len(self.all) < 4:
            if np.random.random(1) < 0.03:
                new_trash = Trash(64,64)
                new_trash.create()
                self.all.append(new_trash)

class Trash(object):
    def __init__(self,width,height):
        self.x = np.random.randint(game.width - 100)
        self.y = -100
        self.width = width
        self.height = height
        self.hitbox = (self.x , self.y, self.width, self.height)

    def create(self):
        self.move()
        trash_blit = game.window.blit(trash, (self.x,self.y))
        self.hitbox = (self.x , self.y, self.width, self.height)
        pygame.draw.rect(game.window,(255,0,0),self.hitbox,2)
        pygame.display.update(trash_blit)
    
    def move(self):
        self.y += 5
        if self.y > 600:
            self.y -= 700
            self.x = np.random.randint(game.width - 100)

game = Game(840,650,"Car crash")

# global images
curveRight = pygame.image.load('car2R.png').convert_alpha()
curveLeft = pygame.image.load('car2L.png').convert_alpha()
curveBottom = pygame.image.load('car2B.png').convert_alpha()
carNormal = pygame.image.load("car2.png").convert_alpha()
lifes = pygame.image.load("lifes.png").convert_alpha()
background_img = pygame.image.load("bg.png").convert_alpha()
trash = pygame.image.load("trash.png").convert_alpha()
running = True


car = Car((game.height-100),(game.width/2),64,64,20)
obstacles = Obstacles()

speed = 0
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
    
    for obstacle in obstacles.all:
        obstacle.create()
        if car.collide(obstacle):
            print('BATEU')
    
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
        car.y = car.y + car.vel+6
        car.left = False
        car.right = False
        car.bottom = True     
        scrollY(game.bg, 5)
    
    game.start(speed)
    clock.tick(30)
    pygame.display.update()
pygame.quit()