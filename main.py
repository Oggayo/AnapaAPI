import turtle as t


class Hero:
    def forward(self, forward):
        t.forward(forward)

    def left(self, forward):
        t.left(90)
        t.forward(forward)

    def right(self, forward):
        t.forward(90)
        t.forward(forward)

    def back(self, forward):
        t.back(forward)


class Draw:
    def tree(self, height, width):
        t.left(90)
        t.forward(height)
        t.right(90)

        t.right(width)
        t.right(90)

        t.forward(height)
        t.right(90)

        t.forward(width)
        t.penup()
        t.right(90)
        t.forward(height)

        t.right(90)
        t.forward(width / 2)
        t.pendown()
        t.circle(width * 3)

    def house(self, height, width):
        t.forward(width)

        t.right(90)
        t.forward(height)

        t.right(90)
        t.forward(width)

        t.right(90)
        t.forward(height)

        t.right(45)
        t.forward(width)

        t.right(115)
        t.forward(width)

    def car(self, height, width):
        t.forward(width)
        t.right(90)

        t.forward(height)
        t.right(90)

        t.forward(width)
        t.right(90)

        t.forward(height)
        t.right(90)

        t.forward(width * 0.33)
        t.left(90)
        t.forward(height * 0.5)
        t.right(90)
        t.forward(width * 0.33)
        t.right(90)
        t.forward(height * 0.5)
        t.left(90)
        t.forward(width * 0.33)
        t.right(90)
        t.forward(height)
        t.right(90)

        t.forward(width * 0.25)
        t.circle(height * 0.45)
        t.forward(width * 0.25)
        t.circle(height * 0.45)


hero = Hero()
draw = Draw()
hero_or_draw = int(input('1 или 2? - '))

if hero_or_draw == 1:
    while True:
        person_choice = int(input('Куда идти?\n1 - вперед\n2 - влево\n3 - вправо\n4 - назад\n'))
        person_choice_forward = int(input('Насколько идти? - '))
        if person_choice == 1:
            hero.forward(person_choice_forward)
        elif person_choice == 2:
            hero.left(person_choice_forward)
        elif person_choice == 3:
            hero.right(person_choice_forward)
        elif person_choice == 4:
            hero.back(person_choice_forward)
        else:
            print('Товарищ, ты не прав, либо 1, либо 2, либо 3, либо 4, другого не дано')
else:
    while True:
        person_choice = int(input('Машина, дом или дерево? (1, 2, 3 - '))
        if person_choice == 1:
            draw_car = int(input('Высота - ')), int(input('Ширина - '))
        elif person_choice == 2:
            draw_house = int(input('Высота - ')), int(input('Ширина - '))
            print('Крутецкий дом')
        elif person_choice == 3:
            draw_tree = int(input('Высота - ')), int(input('Ширина - '))

