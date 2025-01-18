import pygame
import csv
import os


pygame.init()

screen_x = 1280; screen_y = 768
size_tile = 16

dim_x = int(screen_x / size_tile) 
dim_y = int(screen_y / size_tile) 
mov = size_tile

class tile(pygame.sprite.Sprite):
    def __init__(self, ID, x, y):
        super().__init__()
        self.ID = ID
        self.x = x
        self.y = y
        self.img = pygame.image.load(f"tileset/{ID}.png").convert()

    def draw(self, layer, movex=0, movey=0):
        layer.blit(self.img, ((self.x - movex)*size_tile, (self.y - movey)*size_tile, size_tile, size_tile))


class tilemap:
    def __init__(self, screen):
        """
        self.x and self.y are the camera position
        """
        self.backlayer = pygame.Surface((screen.get_width(), screen.get_height()))
        self.alltile = self.read_csv("map1.csv")
        self.x = 0
        self.y = 0
        self.build()
        
    def read_csv(self, file):
        """
        return a 'matrix' [colums y][line x]
        the matrix contain a single tile of tilemap
        the tile has position (x,y)
        """
        alltile = list()
        with open(os.path.join(file)) as data:
            data = list(csv.reader(data, delimiter = ','))
            for y in range(0,len(data)):
                rowtile = list()
                for x in range(0, len(data[y])):
                    rowtile.append(tile(data[y][x], x, y))
                alltile.append(rowtile)
                
        return alltile
    def build(self):
        """
        this function build the tilemap, tile for tile, every frame.
        (but only draw the tiles in the screen)
        """
        self.backlayer.fill((0,0,0))
        for y in range(self.y, self.y + dim_y):
            for x in range(self.x, self.x + dim_x):
                self.alltile[y][x].draw(self.backlayer, self.x, self.y)

    def draw(self, screen):
        self.build()
        screen.blit(self.backlayer, (0,0))

    def move(self, dx, dy):
        """
        move the camera position (self.x, self.y) of dx and dy
        (this function check if the self.x and self.y get off the borders)
        """
        self.x = max(0, min(self.x - dx, len(self.alltile[0]) - dim_x))
        self.y = max(0, min(self.y - dy, len(self.alltile) - dim_y))





screen = pygame.display.set_mode((screen_x, screen_y))

backlayer = tilemap(screen)
backlayer.draw(screen)

delay = pygame.time.Clock()

run = 1
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0
            
    #it move of 1 tile
    mov = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        mov = True
        backlayer.move(1, 0)
    elif keys[pygame.K_RIGHT]:
        mov = True
        backlayer.move(-1, 0)
    elif keys[pygame.K_UP]:
        mov = True
        backlayer.move(0,1)
    elif keys[pygame.K_DOWN]:
        mov = True
        backlayer.move(0,-1)
    #update the screen if move
    if mov:
        backlayer.draw(screen)
    delay.tick(30)
    pygame.display.update()


pygame.quit()