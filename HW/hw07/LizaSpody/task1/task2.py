def triangle():
    base = writeNumber('base')
    height = writeNumber('height')
    return 0.5 * base * height


def rectangle():
    a = writeNumber('first side')
    b = writeNumber('second side')
    return a * b


def circle():
    r = writeNumber('radios')
    return 3.14 * r ** 2


def writeNumber(name):
    answer = input(f'Write {name}: ')
    while not answer.isdigit():
        answer = input(f'Write {name} (NUMBER!!!!): ')
    return float(answer)


def task():
    num = input('Choose a number what you want: 1-triangle, 2-rectangle, 3-circle: ')
    if num == '1':
        return print(triangle())
    elif num == '2':
        return print(rectangle())
    elif num == '3':
        return print(circle())
    else:
        return print('You wrote uncorrected number')


task()
