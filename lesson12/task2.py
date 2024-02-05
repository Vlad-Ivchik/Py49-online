class BeeElephant:
    def __init__(self, bee, elephant):
        if not isinstance(bee, int) or not isinstance(elephant, int):
            raise TypeError
        else:
            self.bee = bee
            self.elephant = elephant

    def fly(self):
        if self.bee >= self.elephant:
            return True
        else:
            return False

    def trumpet(self):
        if self.elephant >= self.bee:
            return "tu-tu-doo-doo"
        else:
            return "wzzzz"

    def eat(self, meal, value):
        if not meal == 'nectar' and not meal == 'grass':
            raise TypeError
        if meal == 'nectar':
            self.bee += value
            self.elephant -= value
        elif meal == 'grass':
            self.bee -= value
            self.elephant += value
        if self.elephant > 100:
            self.elephant = 100
        elif self.elephant < 0:
            self.elephant = 0
        if self.bee > 100:
            self.bee = 100
        elif self.bee < 0:
            self.bee = 0

        return self.bee, self.elephant


bee_elephant = BeeElephant(6, 7)

bee_elephant.eat('nectar', 6)

print(bee_elephant.eat("nectar", 3))
print(bee_elephant.eat("grass", 7))
