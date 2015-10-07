from character import Character
from monster import Goblin
from monster import Troll
from monster import Dragon


class Game:
    def setup(self):
        self.player = Character()
        self.monsters = [
            Goblin(),
            Troll(),
            Dragon()
        ]
