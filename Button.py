import pygame

class Button:
    def __init__(self, scr: pygame.Surface, rect: pygame.Rect | tuple[int, int, int, int], color: tuple[int, int, int],
                 btn_text: str, btntext_color: tuple[int, int, int], on_click,
                 border_thickness: int = 5, border_color: tuple[int, int, int] = (255, 255, 255)) -> None:

        self.screen = scr
        self.rect = pygame.Rect(rect)
        self.color = color
        self.text = btn_text
        self.text_color = btntext_color
        self.on_click = on_click

        self.active = True
        self.show = True

        self.border_thickness = border_thickness
        self.border_color = border_color
        return

    def handle(self) -> None:
        if self.show:
            pygame.draw.rect(self.screen, self.border_color,
                             (self.rect[0] - self.border_thickness, self.rect[1] - self.border_thickness,
                              self.rect[2] + (self.border_thickness * 2), self.rect[3] + (self.border_thickness * 2)))

            pygame.draw.rect(self.screen, self.color, self.rect)

            btn_font = pygame.font.Font("files/Raleway-VariableFont_wght.ttf", self.rect[3] - (self.rect[3] // 3))

            textobj = btn_font.render(self.text, True, self.text_color)
            textobj_rect = textobj.get_rect()

            textobj_rect.center = (self.rect[0] + self.rect[2] // 2, self.rect[1] + self.rect[3] // 2)

            self.screen.blit(textobj, textobj_rect)

            mouse_pos = pygame.mouse.get_pos()
            if self.rect.colliderect((mouse_pos[0], mouse_pos[1], 1, 1)) and self.active:
                for e in pygame.event.get():
                    if e.type == pygame.MOUSEBUTTONDOWN:
                        self.on_click()

            return


if __name__ == "__main__":
    print("i am so niche twin ✌️")
