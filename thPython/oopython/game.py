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
        self.monster = self.get_next_monster()

    def get_next_monster(self):
        try:
            return self.monsters.pop(0)
        except IndexError:
            return None

    def monster_turn(self):
        
