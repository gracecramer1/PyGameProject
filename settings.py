class Settings:

    """a class to store all settings for Alien Invasion"""

    def __init__(self):
        """initialize the game's settings"""
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (230, 230, 230)

        # ship's settings
        self.ship_speed = 1.0
        self.ship_limit = 3

        # bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1.0
