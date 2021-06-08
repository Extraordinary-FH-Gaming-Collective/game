class TextDrawer:
    def __init__(self, screen):
        self.screen = screen

    def draw(self, text, font, color, x, y):
        text_obj = font.render(text, 1, color)
        text_rect = text_obj.get_rect()
        text_rect.topleft = (x, y)
        self.screen.blit(text_obj, text_rect)
