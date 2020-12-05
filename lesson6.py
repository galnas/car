# import pygame

# pygame.init()

# gameDisplay = pygame.display.set_mode((800,600))
# pygame.display.set_caption('A bit Racey')

# clock = pygame.time.Clock()

# crashed = False

# while not crashed:

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             crashed = True

#         print(event)

#     pygame.display.update()
#     clock.tick(60)

# pygame.quit()
# quit()

# import pygame


# pygame.init()


# display_width = 800
# display_height = 600

# gameDisplay = pygame.display.set_mode((display_width,display_height))
# pygame.display.set_caption('A bit Racey')

# black = (0,0,0)
# white = (255,255,255)

# clock = pygame.time.Clock()
# crashed = False
# carImg = pygame.image.load('racecar.png')

# def car(x,y):
#     gameDisplay.blit(carImg, (x,y))

# x =  (display_width * 0.45)
# y = (display_height * 0.8)

# while not crashed:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             crashed = True

#     gameDisplay.fill(white)
#     car(x,y)

        
#     pygame.display.update()
#     clock.tick(60)

# pygame.quit()
# quit()


import pygame

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load('racecar.png')
Ball_Img = pygame.image.load('ball.png')
Green_Img = pygame.image.load('green.png')

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

def Ball(x,y):
    gameDisplay.blit(Ball_Img, (x,y))

def Green(x,y):
    gameDisplay.blit(Green_Img, (x,y))

x =  (display_width * 0.5)
y = (display_height * 0.5)
x_change = 0
y_change = 0
Green (display_width * 0.35, display_height * 0.15)
# spaw = False
car_speed = 0
ball_speed = 0

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        ############################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
            elif event.key == pygame.K_UP:
                y_change = -5
            elif event.key == pygame.K_DOWN:
                y_change = 5
            # elif event.key == pygame.K_SPAWN:
            #     spawn = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            elif event.key == pygame.K_UP:
                y_change = 0
            elif event.key == pygame.K_DOWN:
                y_change = 0
        ######################
    ##
    x += x_change
    y += y_change
   ##         
    gameDisplay.fill(white)
    car(x,y)
    
    Ball (x,y)

    

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()