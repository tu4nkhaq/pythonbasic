
import pygame , sys
def floor_pos():
    screen.blit(floor,(floor_x_pos,600))
    screen.blit(floor,(floor_x_pos+432,600))
pygame.init()
screen=pygame.display.set_mode((432,768))
pygame.display.set_caption("Flappy Bird By Khang")
clock=pygame.time.Clock()
gravity=0.25
bird_movement=0
### background
bg=pygame.image.load('flappybird/assets/background-night.png')
bg=pygame.transform.scale2x(bg)
floor=pygame.image.load('flappybird/assets/floor.png')
floor=pygame.transform.scale2x(floor)
floor_x_pos=0
bird=pygame.image.load('flappybird/assets/yellowbird-midflap.png')
bird=pygame.transform.scale2x(bird)
bird_rect=bird.get_rect(center=(100,384))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement=0
                bird_movement -= 5
    screen.blit(bg,(0,0))
    bird_movement+=gravity
    bird_rect.centery+=bird_movement
    screen.blit(bird,bird_rect)
    floor_x_pos-=1
    floor_pos()
    if floor_x_pos<=-432:
        floor_x_pos=0
    pygame.display.update()
    clock.tick(120)
