from game_classes.human import Human

class Pirate(Human):
    def __init__(self,name):
        super().__init__()
        self.mana = 1
        self.strength = 7
        self.name = name
        self.rum = "bottle of rum"

    def parry(self):
        print(f"{self.name} has parried the attack")

    def chug_rum(self):
        super().heal()
        print(f"The Pirate looks at their {self.rum} and it fills them with brute force (Strength +3)")
        self.strength += 3

    def heal(self):
        super().heal()
        print(f"The healing cost you one point of armor")
        self.armor-= 1