import pygame
import sys

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
GREEN = (0, 255, 0)
LIGHT_GREEN = (144, 238, 144)

# Button class
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, text_color, font, visibility):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.hover_text_color = LIGHT_GREEN
        self.font = font
        self.is_hovered = False
        self.visible = visibility
    
    def draw(self, surface):
        if self.visible:
            if self.is_hovered:
                pygame.draw.rect(surface, self.hover_color, self.rect)
            else:
                pygame.draw.rect(surface, self.color, self.rect)
            pygame.draw.rect(surface, BLACK, self.rect, 2)
            
            if self.is_hovered:
                font_color = self.hover_text_color
            else:
                font_color = self.text_color
            
            font_surface = self.font.render(self.text, True, font_color)
            font_rect = font_surface.get_rect(center=self.rect.center)
            surface.blit(font_surface, font_rect)
    
    def update_hover(self, pos):
        self.is_hovered = self.rect.collidepoint(pos)