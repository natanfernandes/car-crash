import pygame
import time
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
        self.game_font = pygame.font.Font("font/PressStart2P-Regular.ttf", 25)
        self.player_lifes = 3
        self.life_positions = [(50,50),(100,50),(150,50)]
        self.bg = pygame.image.load("bg.png").convert_alpha()
        self.restarting = False
    
    def start(self,move):
        self.window.blit(self.bg, (0, move))
        
        if self.restarting:
            self.bg_move('STOP')
        else:
            self.bg_move('START')
        
        batidas = self.game_font.render('Batidas:' + str(car.crashCount), 1, (255,0,0))
        self.window.blit(batidas,(500,50))
       
        self.display_lifes()
        obstacles.create()
      
        if car.left:
            car.create(curveLeft)
        elif car.right:
            car.create(curveRight)
        elif car.bottom:
            car.create(curveBottom)
        else:
            car.create(carNormal)

    def bg_move(self,condition):
        if condition == 'STOP':
            scrollY(self.bg,0)
        else:
            if car.crashCount >= 3:
                scrollY(self.bg,0)
            else:
                scrollY(self.bg, 20)

    def display_lifes(self):
        for position in self.life_positions:
            game.window.blit(lifes,position)
    
        

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
        # pygame.draw.rect(game.window,(255,0,0),self.hitbox,2)
        
    
    def hit(self):
        self.crashCount += 1
        self.move_to_start()
        if len(game.life_positions)> 0:
            game.life_positions.pop()
        game.player_lifes -=1
        obstacles.all = []
        obstacles.trashs = []
        obstacles.rocks = []
        game.restarting = True
        
    def in_road(self,side):
        if side == 'L':
            if self.x > self.vel+130:
                return True
            else:
                return False
        elif side == 'R':
            if self.x < (game.width - self.width - 150):
                return True
            else:
                return False
    
    def move_to_start(self):
        self.x = (game.width/2)
        self.y = (game.height-100)

    def move(self,orientation):
        if orientation == 'L':
            self.x = self.x - self.vel
            self.left = True
            self.right = False
            self.bottom = False

        elif orientation == 'R':
            self.x = self.x + self.vel
            self.left = False
            self.right = True
            self.bottom = False

        elif orientation == 'UP':
            self.y = self.y - self.vel
            self.left = False
            self.right = False
            self.bottom = False

        elif orientation == 'DOWN':
            self.y = self.y + self.vel
            self.left = False
            self.right = False
            self.bottom = True     

    def collide(self,obstacle):

        #check collision with obtacles 64x64
        if obstacle.hitbox[2] == 64 and obstacle.hitbox[3] == 64:
            if (car.y - car.height/2) < (obstacle.hitbox[1] + obstacle.hitbox[3]/2) and (car.y -car.height/2) > (obstacle.hitbox[1] - obstacle.hitbox[3]/2):
                if(car.x + car.width/2) > (obstacle.hitbox[0]-obstacle.hitbox[2]/2) and (car.x + car.width/2) < (obstacle.hitbox[0]+obstacle.hitbox[2]/2):
                    return True
                elif(car.x-car.width/2) < (obstacle.hitbox[0]+obstacle.hitbox[2]/2) and (car.x + car.width/2) > (obstacle.hitbox[0]+obstacle.hitbox[2]/2):
                    return True
                else:
                    return False
            elif ((car.y + car.height/2)< (obstacle.hitbox[1] + obstacle.hitbox[3]/2) and (car.y + car.height/2) > (obstacle.hitbox[1] - obstacle.hitbox[3]/2)):
                if(car.x + car.width/2) > (obstacle.hitbox[0]-obstacle.hitbox[2]/2) and (car.x + car.width/2) < (obstacle.hitbox[0]+obstacle.hitbox[2]/2):
                    return True
                elif(car.x-car.width/2) < (obstacle.hitbox[0]+obstacle.hitbox[2]/2) and (car.x + car.width/2) > (obstacle.hitbox[0]+obstacle.hitbox[2]/2):
                    return True
                else:
                    return False
            else:
                return False
        
        #check collision with obstacles 128x128
        else:
            if (car.y - car.height/2) < (obstacle.hitbox[1] + obstacle.hitbox[3]/2) and (car.y -car.height/2) > (obstacle.hitbox[1] - obstacle.hitbox[3]/2):
                if(car.x + car.width/2) > (obstacle.hitbox[0]-obstacle.hitbox[2]/4) and (car.x + car.width/2) < (obstacle.hitbox[0]+obstacle.hitbox[2]/4):
                    return True
                elif(car.x-car.width) < (obstacle.hitbox[0]+obstacle.hitbox[2]/2) and (car.x + car.width) > (obstacle.hitbox[0]+obstacle.hitbox[2]/2):
                    return True
                else:
                    return False
            elif ((car.y + car.height/2) < (obstacle.hitbox[1] + obstacle.hitbox[3]/4) and (car.y + car.height/2) > (obstacle.hitbox[1] - obstacle.hitbox[3]/4)):
                if(car.x + car.width/2) > (obstacle.hitbox[0]-obstacle.hitbox[2]/4) and (car.x + car.width/2) < (obstacle.hitbox[0]+obstacle.hitbox[2]/4):
                    return True
                elif(car.x-car.width/2) < (obstacle.hitbox[0]+obstacle.hitbox[2]/4) and (car.x + car.width/2) > (obstacle.hitbox[0]+obstacle.hitbox[2]/4):
                    return True
                else:
                    return False
            else:
                return False
       

class Obstacles(object):
    def __init__(self):
        self.all = []
        self.trashs = []
        self.rocks = []
    
    def spawn_obstacles(self):
        if len(self.trashs) < 4:
            if np.random.random(1) < 0.03:
                new_trash = Trash(64,64)
                new_trash.create()
                self.all.append(new_trash)
                self.trashs.append(new_trash)
        
        if len(self.rocks) < 2:
            if np.random.random(1) < 0.03:
                rock = Rock(128,128)
                rock.create()
                self.all.append(rock)
                self.rocks.append(rock)
            
    def create(self):
        self.spawn_obstacles()
        
        #remove all obstacles if max crash nums        
        if car.crashCount >= 3:
            self.all = []
            self.trashs = []
            self.rocks = []

class Trash(object):
    def __init__(self,width,height):
        self.x = np.random.randint(190,game.width - 200)
        self.y = -150
        self.width = width
        self.height = height
        self.hitbox = (self.x , self.y, self.width, self.height)

    def create(self):
        self.move()
        print(self.x)
        trash_blit = game.window.blit(trash, (self.x,self.y))
        self.hitbox = (self.x , self.y, self.width, self.height)
        # pygame.draw.rect(game.window,(0,0,0,0),self.hitbox,1)
        pygame.display.update(trash_blit)
    
    def move(self):
        self.y += 5
        if self.y > 650:
            self.y -= 800
            self.x = np.random.randint(190,game.width - 200)
            print(self.x)

class Rock(object):
    def __init__(self,width,height):
        self.x = np.random.randint(190,game.width - 200)
        self.y = -150
        self.width = width
        self.height = height
        self.hitbox = (self.x , self.y, self.width, self.height)

    def create(self):
        self.move()
        rock_blit = game.window.blit(rock, (self.x,self.y))
        # pygame.draw.rect(game.window,(0,0,0),self.hitbox,1)
        self.hitbox = (self.x , self.y, self.width, self.height)
        pygame.display.update(rock_blit)
    
    def move(self):
        self.y += 5
        if self.y > 650:
            self.y -= 800
            self.x = np.random.randint(190,game.width - 200)
            print(self.x)

# start the game
game = Game(840,650,"Car crash")

# global images
curveRight = pygame.image.load('car2R.png').convert_alpha()
curveLeft = pygame.image.load('car2L.png').convert_alpha()
curveBottom = pygame.image.load('car2B.png').convert_alpha()
carNormal = pygame.image.load("car2.png").convert_alpha()
lifes = pygame.image.load("lifes2.png").convert_alpha()
background_img = pygame.image.load("bg.png").convert_alpha()
trash = pygame.image.load("t.png").convert_alpha()
rock = pygame.image.load("rock.png").convert_alpha()
running = True


car = Car((game.height-100),(game.width/2),64,64,20)
obstacles = Obstacles()
start_time = pygame.time.get_ticks()
restart_time = 5
speed = 0
while running:
    current_time = pygame.time.get_ticks()
    if game.restarting:
        if restart_time > 0:
            batidas = game.game_font.render('Você bateu, voltando em :' + str(restart_time), 1, (255,0,0))
            game.window.blit(batidas,(100,250))
            pygame.display.update()
            print(current_time - start_time,restart_time,game.restarting)
            if current_time - start_time > 1000:
                restart_time -= 1
                start_time = current_time
                obstacles.all = []
                obstacles.trashs = []
                obstacles.rocks = []
        else :
            game.restarting = False
            restart_time = 5
            obstacles.all = []
            obstacles.trashs = []
            obstacles.rocks = []
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
    
    
    for obstacle in obstacles.all:
        if car.crashCount < 4:
            obstacle.create()

        if car.collide(obstacle):
            car.hit()
            
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and car.in_road('L'):
        car.move('L')

    if keys[pygame.K_RIGHT] and car.in_road('R'):
        car.move('R')

    if keys[pygame.K_UP] and car.y > 0:
        car.move('UP')

    if keys[pygame.K_DOWN] and car.y < (game.height - car.height-20):
        car.move('DOWN')
    
    game.start(speed)
    clock.tick(30)
    pygame.display.update()

pygame.quit()