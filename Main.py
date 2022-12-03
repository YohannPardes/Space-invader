import pygame
import random

pygame.init()

WIDTH = HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
IMG = pygame.image.load("Space.jpg")
factor = 1/7
IMG = pygame.transform.scale(IMG, (int(IMG.get_width()*factor), int(IMG.get_width()*factor)))
pygame.display.flip()
clock = pygame.time.Clock()

class Elements:

    elem_liste = []
    def __init__(self):

        self.pos = None
        self.spd = None
        self.color = None
    
        # self.img = None

    def show(self, screen):
        
        new_x = self.x - self.img.get_width()/2
        new_y = self.y - self.img.get_height()/2
        # pygame.draw.circle(screen, self.color, self.pos, 20)
        pygame.Surface.blit(screen, self.img, (new_x, new_y))
        

    @classmethod
    def show_all(cls, screen):
        
        for elem in cls.elem_liste:

            elem.show(screen)

class Ennemies(Elements):

    def __init__(self):

        super().__init__()

        self.enem_liste = []

        self.ligne_num = 2
        self.enemies_per_ligne = 10

        self.spd = 1.5
        self.rad = 55

    def init_enemies(self):
        
        for i in range(self.ligne_num):
            for j in range(self.enemies_per_ligne):

                x = WIDTH//(self.enemies_per_ligne + 2)*(j+1) -25
                y = self.rad * (i + 1)

                self.enem_liste.append(Ennemie([x, y], self.spd))

    def moveAll(self):
        move = False
        for enem in self.enem_liste:
            if enem.move():
                move = True
        
        if move:
            for enem in self.enem_liste:
                enem.y += WIDTH//50
                enem.spd *=-1
                

class Ennemie(Ennemies):

    def __init__(self, pos, spd):

        super().__init__()

        temp_img = pygame.image.load("AlienG.png")
        factor = 0.05
        self.img = pygame.transform.scale(temp_img, (int(temp_img.get_width()*factor), int(temp_img.get_width()*factor)))
        self.pos = pos
        self._x = pos[0] 
        self._y = pos[1] 
        
        self.spd = spd
        self.color = (255, 40, 40)

        Elements.elem_liste.append(self)

    def move(self):

        self.x += self.spd

        if not 0+self.rad/2 <self.x< WIDTH-self.rad/2:
            return True


    @property
    def x(self):
        return self.pos[0]

    @property
    def y(self):
        return self.pos[1]

    @x.setter
    def x(self, val):
        self.pos[0] = val

    @y.setter
    def y(self, val):
        self.pos[1] = val


def show_frame(screen):
    screen.blit(IMG, (0,0))
    Elements.show_all(screen)
    pygame.display.flip()
    clock.tick(120)


E = Ennemies()
E.init_enemies()

done = False
frameCount = 0
while not done:
    show_frame(screen)
    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pass

    E.moveAll()
