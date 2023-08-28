import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """класс для управления кораблем"""

    def __init__(self, ai_game):
        """инициализирует корабль и задает его начальную позицию"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # загружает изображение корабля и получает прямоугольник
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # каждый новый корабль появляется у нижнего края
        self.rect.midbottom = self.screen_rect.midbottom

        # сохранение вещественной координаты центра корабля
        self.x = float(self.rect.x)

        # флаги перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """обновляет позицию корабля с учетом флагов"""
        # Обновляется атрибут х объекта ship, не rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed_factor

        # обновление атрибута rect на основании self.x
        self.rect.x = self.x

    def blitme(self):
        """рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """азмещает корабль в центре нижней стороны"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)