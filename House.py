import turtle as t


class House:
    def create_roof(self, long, width):
        return f'Roof was create - {long}, {width}'

    def create_wall(self, width, height):
        return f'Wall was create - {width, height}'


h = House()
print(h.create_roof(100, 200))
print(h.create_wall(100, 100))
