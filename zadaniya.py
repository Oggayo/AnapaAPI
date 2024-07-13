import turtle


def move_turtle():
    direction = input('Введите направление (вперед, назад, влево, вправо): ')
    distance = int(input('Введите расстояние: '))

    if direction == 'вперед':
        turtle.forward(distance)
    elif direction == 'назад':
        turtle.backward(distance)
    elif direction == 'влево':
        turtle.left(distance)
    elif direction == 'вправо':
        turtle.right(distance)
    else:
        print('Некорректное направление: ')
    t = turtle.Turtle()
    while True:
        move_turtle()
