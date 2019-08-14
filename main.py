import pygame
import numpy as np  
pygame.init()

clock = pygame.time.Clock()

def scrollX(screenSurf, offsetX):
    width, height = screenSurf.get_size()
    copySurf = screenSurf.copy()
    screenSurf.blit(copySurf, (offsetX, 0))
    if offsetX < 0:
        screenSurf.blit(copySurf, (width + offsetX, 0), (0, 0, -offsetX, height))
    else:
        screenSurf.blit(copySurf, (0, 0), (width - offsetX, 0, offsetX, height))

def scrollY(screenSurf, offsetY):
    width, height = screenSurf.get_size()
    copySurf = screenSurf.copy()
    screenSurf.blit(copySurf, (0, offsetY))
    if offsetY < 0:
        screenSurf.blit(copySurf, (0, height + offsetY), (0, 0, width, -offsetY))
    else:
        trash.create()
        if trash.y > height:
            teste = newTrash()
            print('cria dnv')
        screenSurf.blit(copySurf, (0, 0), (0, height - offsetY, width, offsetY))
def newTrash():
    a = Trash(64,64)
    return a.create()
class Game(object):
    def __init__(self,width,height,title):
        self.window = pygame.display.set_mode((width,height))
        self.width = width
        self.height = height
        self.title = title
        self.caption = pygame.display.set_caption(title)
        self.game_font = pygame.font.SysFont("Times New Roman", 25)
        self.player_lifes = 3
        self.bg = pygame.image.load("bg.png")
    
    def start(self,move):
        self.window.blit(self.bg, (0, move))
        scrollY(self.bg, 20)
        batidas = self.game_font.render('Batidas:', 1, (255,0,0))
        qtd = self.game_font.render(str(car.crashCount), 1, (255,0,0))
        self.window.blit(batidas,(500,50))
        self.window.blit(qtd,(600,50))
        life_positions = [(50,50),(100,50),(150,50)]

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

        pygame.display.update()

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
        self.hitbox = (self.x + 20, self.y, self.width, self.height)
    
    def create(self,img):
        car_surface = pygame.Surface((64,64))  
        car_surface.set_alpha(0)  
        car_surface.fill((255,255,255))
        game.window.blit(car_surface, (self.x,self.y))
        game.window.blit(img, (self.x,self.y))
        self.hitbox = (self.x , self.y, self.width, self.height)
        pygame.draw.rect(game.window,(255,0,0),self.hitbox,2)

    def hit(self):
        self.crashCount += 1
        print('bateu')

class Trash(object):
    def __init__(self,width,height):
        self.x = np.random.randint(game.width - 100)
        self.y = np.random.randint(game.height - 100)
        self.width = width
        self.height = height
        self.hitbox = (self.x , self.y, self.width, self.height)

    def create(self):
        trash_image = pygame.image.load("trash.png")
        print(game.bg.get_width())
        self.y += 5
        trash_surface = pygame.Surface((64,64))  
        trash_surface.set_alpha(0)  
        trash_surface.fill((255,255,255))
        
        game.window.blit(trash_surface, (self.x,self.y))
        game.window.blit(trash_image, (self.x,self.y))
        self.hitbox = (self.x , self.y, self.width, self.height)
        pygame.draw.rect(game.window,(255,0,0),self.hitbox,2)
        pygame.display.update()

# global images
curveRight = pygame.image.load('r3.png')
curveLeft = pygame.image.load('l3.png')
curveBottom = pygame.image.load('b3.png')
carNormal = pygame.image.load("car.png")
lifes = pygame.image.load("lifes.png")

running = True

game = Game(1000,600,"Car crash")

car = Car((game.height-100),(game.width/2),64,64,20)
trash = Trash(64,64)
speed = 0
while running:
    clock.tick(20)
    #detect events in game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    #collider check ps:eu q fiz to mt feliz         
    if (car.y - car.height/2) < (trash.hitbox[1] + trash.hitbox[3]/2) and (car.y -car.height/2) > (trash.hitbox[1] - trash.hitbox[3]/2):
        if(car.x + car.width/2) > (trash.hitbox[0]-trash.hitbox[2]/2) and (car.x + car.width/2) < (trash.hitbox[0]+trash.hitbox[2]/2):
            car.hit()
            print('bateu 1')
        elif(car.x-car.width/2) < (trash.hitbox[0]+trash.hitbox[2]/2) and (car.x + car.width/2) > (trash.hitbox[0]+trash.hitbox[2]/2):
            car.hit()
            print('bateu 2')
        else:
            print('passou do y mas n do x')
    elif ((car.y + car.height/2)< (trash.hitbox[1] + trash.hitbox[3]/2) and (car.y + car.height/2) > (trash.hitbox[1] - trash.hitbox[3]/2)):
        if(car.x + car.width/2) > (trash.hitbox[0]-trash.hitbox[2]/2) and (car.x + car.width/2) < (trash.hitbox[0]+trash.hitbox[2]/2):
            car.hit()
            print('bateu 1/2')
        elif(car.x-car.width/2) < (trash.hitbox[0]+trash.hitbox[2]/2) and (car.x + car.width/2) > (trash.hitbox[0]+trash.hitbox[2]/2):
            car.hit()
            print('bateu 2/2')
        else:
            print('passou do y mas n do x2')
    else:
        print('nada')
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
        scrollY(game.bg, 5)

    game.start(speed)


pygame.quit()