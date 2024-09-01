# Примеры


class Monster:

    def __init__(self, level: int):
        self.level = level
        self.health_points = 100 * level
        self.attack_power = 50 * level

    def attack(self):
        return f"Monster attack with power {self.attack_power}"


my_monster = Monster(level=7)
my_monster.level  # -> 7
my_monster.health_points  # -> 700
my_monster.attack_power  # -> 350

my_monster.attack()  # -> Monster attack with power 350
