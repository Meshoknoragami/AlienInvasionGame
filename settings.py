class Settings():
    """класс для хранения всех настроек игры Alien Invasion"""

    def __init__(self):
        """Инициализирует настройки игры"""
        # параметры экрана
        self.screen_width = 1340
        self.screen_height = 680
        self.bg_color = (255,255,255)

        # настройки корабля
        self.ship_limit = 3

        # параметры снаряда
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 87, 32)
        self.bullets_allowed = 3

        # настройки пришельцев
        self.fleet_drop_speed = 10

        # темп ускорения игры
        self.speedup_scale = 1.1
        # темп роста стоимости пришельцев
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ инициализирует настройки, изменяющиеся в ходе игры"""
        self.ship_speed_factor = 1.5
        self.bullet_speed = 3
        self.alien_speed_factor = 1.0

        # fleet_direction = 1 обозначает движение вправо, а -1 - влево
        self.fleet_direction = 1

        # подсчёт очков
        self.aliens_points = 50

    def increase_speed(self):
        """увеличивает настройки скорости и стоимости пришельцев"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.aliens_points = int(self.aliens_points * self.score_scale)
