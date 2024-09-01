# Примеры


class Ork:

    def __init__(self, level: int):
        self.level = level
        self.health_points = 100 * level
        self.attack_power = 50 * level

    def attack(self):
        return f"Ork attack with power {self.attack_power}"

    def __str__(self):
        return f"Ork (level:{self.level}) (health_points: {self.health_points})"


my_ork = Monster(level=7)

my_ork.level  # -> 7
my_ork.health_points  # -> 700
my_ork.attack_power  # -> 350

my_ork.attack()  # -> Ork attack with power 350

my_ork  # -> Ork (level:7) (health_points: 700)


class Elf()
    def __init__(self):
        pass
