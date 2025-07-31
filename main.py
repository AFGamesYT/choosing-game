import pygame

from Button import Button

pygame.init()

WIDTH = 1900
HEIGHT = 900

FPS = 120

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Choosing Game")

clock = pygame.time.Clock()
run = True
fullscreen = False

iteration = 0
MAX_ITERATION = 6
timeline = []

def left_btn_click():
    global iteration, MAX_ITERATION, button_left, button_right, timeline

    if not iteration >= MAX_ITERATION:
        iteration += 1
        timeline.append(0)
        if iteration >= MAX_ITERATION:
            button_left.text = "Die. (Reset)"
            button_right.text = "Die. (Reset)"
    else:
        print(f"You died! Your timeline: {timeline}")
        iteration = 0
        timeline = []
        button_left.text = "Choice 0"
        button_right.text = "Choice 1"


button_left = Button(
        scr=screen, rect=pygame.Rect(200, HEIGHT//2-100, 600, 200), color=[145, 20, 15], on_click_func=left_btn_click,
        image_path=None, btn_text="Choice 1", btntext_color=[0, 0, 0],
        font_path="files/DynaPuff-VariableFont_wdth,wght.ttf", text_size=70, border_thickness=15,
        border_color=[120, 5, 0], corner_radius=20
)

def right_btn_click():
    global iteration, MAX_ITERATION, button_right, button_left, timeline

    if not iteration >= MAX_ITERATION:
        iteration += 1
        timeline.append(1)
        if iteration >= MAX_ITERATION:
            button_left.text = "Die. (Reset)"
            button_right.text = "Die. (Reset)"
    else:
        print(f"You died! Your timeline: {timeline}")
        iteration = 0
        timeline = []
        button_left.text = "Choice 0"
        button_right.text = "Choice 1"


button_right = Button(
    scr=screen, rect=pygame.Rect(WIDTH-800, HEIGHT//2-100, 600, 200), color=[145, 20, 15], on_click_func=right_btn_click,
    image_path=None, btn_text="Choice 2", btntext_color=[0, 0, 0],
    font_path="files/DynaPuff-VariableFont_wdth,wght.ttf", text_size=70, border_thickness=15,
    border_color=[120, 5, 0], corner_radius=20
)

buttons = [button_left, button_right]

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
    for button in buttons:
        button.handle()

    for event in pygame.event.get():
        handle_keyinputs()
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
