class Character:
    experience = 0
    hit_points = 10

    def get_weapom(self):
        weapon_choice = input("Weapon ([S]word, [A]xe, [B]ow): ").lower()
        if weapon_choice in 'sab':
            if weapon_choice == 's':
                return 'sword'
            elif weapon_choice == 'a':
                return 'axe'
            else:
                return 'bow'
        else:
            self.get_weapom()

    def __init__(self, **kwargs):
        self.name = input("Name: ")
        self.weapon = self.get_weapom()

        for key, value in kwargs.items():
            setattr(self, key, value)
