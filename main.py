import pygame

pygame.init()

WIDTH = 2560
HEIGHT = 1440

FPS = 120

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Choosing Game")

clock = pygame.time.Clock()
run = True
fullscreen = True

def handle_keyinputs():
    global fullscreen, screen, run
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_F11:
            fullscreen = not fullscreen
            if fullscreen:
                screen = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE)
            else:
                screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        if event.key == pygame.K_q:
            run = False

main_color = (32, 32, 32)

while run:
    screen.fill(main_color)
    for event in pygame.event.get():
        handle_keyinputs()
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
