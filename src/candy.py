import pygame
import random
from position import Position
from candyphotos import CandyPhotos


class Candy:
    def __init__(self):
        self.id = random.randint(0, 5)
        self.cell_size = 50
        self.row_offset = 0
        self.col_offset = 0
        self.candy = CandyPhotos.load_photos()

    def move(self, row, col):
        self.row_offset += row
        self.col_offset += col

    def get_cell_position(self):
        tile = Position(0, 3)
        tile = Position(tile.row + self.row_offset, tile.col + self.col_offset)
        return tile

    def draw(self, screen, x, y):
        tile = self.get_cell_position()
        tile_rect = pygame.Rect(tile.col * self.cell_size+x, tile.row*self.cell_size+y, self.cell_size-1,
                                self.cell_size-1)
        background_image = pygame.image.load(self.candy[self.id]).convert_alpha()
        background_image = pygame.transform.smoothscale(background_image, (50, 50))
        screen.blit(background_image, tile_rect)
