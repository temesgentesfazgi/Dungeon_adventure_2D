import pygame
from pygame.locals import *
from dungeon import Dungeon
from constants import *
from button import Button

FRAMERATE = 60

SCREEN_RES = WIDTH, HEIGHT = 1200, 800
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)


class GuiView(object):
    def __init__(self, dungeon):

        self.dungeon = dungeon

        pygame.init()

        self.game_surface = pygame.Surface((600, 600))
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        pygame.display.set_caption('Dungeon Adventure')
        self.clock = pygame.time.Clock()
        image1 = pygame.image.load('images/dungeon.png').convert()
        self.screen_bg = pygame.transform.scale(image1, SCREEN_RES)
        # self.bg_game = pygame.image.load('images/bg_game.jpeg').convert()
        
        self.room_width = 100
        self.room_height = 100
        self.door_wall_thick = 20

        self.wall_image = pygame.image.load('images/wall.jpeg').convert()
        self.horiz_wall = pygame.transform.scale(self.wall_image, (self.room_width, self.door_wall_thick // 2))
        self.vert_wall = pygame.transform.scale(self.wall_image, (self.door_wall_thick // 2, self.room_height))

        self.door_image = pygame.image.load('images/door.png').convert()
        self.vert_door = pygame.transform.scale(self.door_image, (self.door_wall_thick // 2, self.room_height))
        # Rotate the image 90 degrees counterclockwise
        self.rotated_door_image = pygame.transform.rotate(self.door_image, 90)
        self.horiz_door = pygame.transform.scale(self.rotated_door_image, (self.room_width, self.door_wall_thick // 2))

        self.grey_cover = pygame.Surface((120, 120))
        self.grey_cover.fill(pygame.Color('darkgrey'))

        self.font = pygame.font.SysFont(None, 20)

        self.north_button = Button(1000, 500, 100, 50, "North", BLACK, GRAY, WHITE, self.font, False)
        self.south_button = Button(1000, 650, 100, 50, "South", BLACK, GRAY, WHITE, self.font, False)
        self.west_button = Button(925, 575, 100, 50, "West", BLACK, GRAY, WHITE, self.font, False)
        self.east_button = Button(1075, 575, 100, 50, "East", BLACK, GRAY, WHITE, self.font, False)

        self.start_new_game_button = Button(100, 200, 120, 50, "Start New Game", BLACK, GRAY, WHITE, self.font, True)
        self.load_button = Button(100, 275, 100, 50, "Load Game", BLACK, GRAY, WHITE, self.font, True)
        self.warrior_button = Button(100, 350, 100, 50, "Warrior", BLACK, GRAY, WHITE, self.font, False)
        self.priestess_button = Button(100, 425, 100, 50, "Priestess", BLACK, GRAY, WHITE, self.font, False)
        self.thief_button = Button(100, 500, 100, 50, "Thief", BLACK, GRAY, WHITE, self.font, False)
        self.use_vision_button = Button(100, 575, 100, 50, "Use Vision Potion", BLACK, GRAY, WHITE, self.font, False)
        self.use_healing_button = Button(100, 650, 100, 50, "Use Healing Potion", BLACK, GRAY, WHITE, self.font, False)

        self.buttons = [self.north_button, self.south_button, self.west_button, self.east_button, 
                        self.start_new_game_button, self.load_button, self.warrior_button, self.priestess_button,
                        self.thief_button, self.use_vision_button, self.use_healing_button]
        
        
    
    def render_text(self, text, pos_x, pos_y):
        font = pygame.font.SysFont(None, 25)
        # Render text onto a surface
        text_surface = font.render(text, True, (255, 255, 255))
        self.screen.blit(text_surface, (pos_x, pos_y))

    
    def draw_buttons(self):
        for button in self.buttons:
            button.draw(self.screen)


    def draw_dungeon(self, init_pos_x, init_pos_y):

        for i, row in enumerate(self.dungeon.rooms):
            pos_y = init_pos_y + (i * (self.door_wall_thick + self.room_height))
            for j, room in enumerate(row):
                pos_x = init_pos_x + (j * (self.door_wall_thick + self.room_width))
                self.draw_room(room, pos_x, pos_y)

                
    
    def draw_room(self, room, pos_x, pos_y):
        thickness = self.door_wall_thick // 2

        if room.neighbors[NORTH] == WALL:
            self.game_surface.blit(self.horiz_wall, (pos_x + thickness, pos_y))
        else:
            self.game_surface.blit(self.horiz_door, (pos_x + thickness, pos_y))

        self.draw_filler(pos_x, pos_y, thickness, thickness)
        self.draw_filler(pos_x + thickness + self.room_width, pos_y, thickness, thickness)


        if room.neighbors[SOUTH] == WALL:
            self.game_surface.blit(self.horiz_wall, (pos_x + thickness, pos_y + thickness + self.room_height))
        else:
            self.game_surface.blit(self.horiz_door, (pos_x + thickness, pos_y + thickness + self.room_height))
        
        self.draw_filler(pos_x, pos_y + thickness + self.room_height, thickness, thickness)
        self.draw_filler(pos_x + thickness + self.room_width, pos_y + thickness + self.room_height, thickness, thickness)


        if room.neighbors[WEST] == WALL:
            self.game_surface.blit(self.vert_wall, (pos_x, pos_y + thickness))
        else:
            self.game_surface.blit(self.vert_door, (pos_x, pos_y + thickness))

        if room.neighbors[EAST] == WALL:
            self.game_surface.blit(self.vert_wall, (pos_x + thickness + self.room_width, pos_y + thickness))
        else:
            self.game_surface.blit(self.vert_door, (pos_x + thickness + self.room_width, pos_y + thickness))

        # if not room.visited_by_player:
        #     self.game_surface.blit(self.grey_cover, (pos_x, pos_y))

    
    def draw_filler(self, pos_x, pos_y, width, height):
        pygame.draw.rect(self.game_surface, (0, 0, 0), (pos_x, pos_y, width, height))
    

    def draw_loop(self):
        while True:
            # Clear the screen
            self.screen.fill((255, 255, 255))
            self.screen.blit(self.screen_bg, (0, 0))

            # self.surface.blit(self.surface_bg, (WIDTH, 0))
            self.screen.blit(self.game_surface, (300, 100))
        
            self.game_surface.fill(pygame.Color('antiquewhite4'))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.MOUSEMOTION:
                    pos = pygame.mouse.get_pos()
                    for button in self.buttons:
                        button.update_hover(pos)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        pos = pygame.mouse.get_pos()
                        if self.north_button.is_hovered:
                            print("North is clicked!")
                        
            
            self.draw_dungeon(0, 0)
            self.draw_buttons()
            pygame.display.flip()
            self.clock.tick(FRAMERATE)

    

    

if __name__ == "__main__":
    dbFile = 'database/monsters.db'
    dungeon = Dungeon(5, 5, dbFile)
    view = GuiView(dungeon)
    view.draw_loop()
    # view.draw()
    # while running:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
    #         elif event.type == KEYDOWN:
    #             if event.key == K_ESCAPE:
    #                 running = False
    #         elif event.type == MOUSEBUTTONDOWN:
    #             row, col = view.convert_mousepos(event.pos)
    #             view.selection = model.get_neighbours(row, col)
    #             view.redraw()
    #     view.blit()