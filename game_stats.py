class GameStats:
    """track stats for alien invasion"""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        # start alien invasion in an inactive state
        self.game_active = True

    def reset_stats(self):
        """initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
