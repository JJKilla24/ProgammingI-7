import pygame
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Placeholder")

x = 50
y = 50
width = 30
height = 30
vel = 5

x = 50
y = 50
width = 30
height = 30
vel = 5

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        x -= vel

    if keys[pygame.K_RIGHT]:
        x += vel

    if keys[pygame.K_UP]:
        y -= vel

    if keys[pygame.K_DOWN]:
        y += vel
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_A]:
        x -= vel

    if keys[pygame.K_D]:
        x += vel

    if keys[pygame.W_]:
        y -= vel

    if keys[pygame.K_S]:
        y += vel

      
    
    win.fill((255,255,255))  # Fills the screen with black
    pygame.draw.rect(win, (255,0,0), (x, y, width, height))   
    pygame.display.update() 
    
pygame.quit()