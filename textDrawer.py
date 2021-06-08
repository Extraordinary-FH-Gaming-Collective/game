class TextDrawer:
    """Creates a Class for writing Text on given Screen."""
    def __init__(self, screen):
        self.screen = screen

    def draw(self, text, font, color, x, y):
        """Draws the given Text on the Screen
        in given Font and Color
        and at given Position
        """

        text_obj = font.render(text, 1, color)
        text_rect = text_obj.get_rect()
        text_rect.topleft = (x, y)
        self.screen.blit(text_obj, text_rect)
