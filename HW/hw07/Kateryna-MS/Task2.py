def area_f():
    '''calculates the area of rectangle, triangle or circle depending on user`s choise'''
    print('Choose which area to calculate: print rectangle or triangle or circle')
    shape = input()

    if shape == "rectangle":
        l = int(input('length: '))
        w = int(input('width: '))
        area = l * w
    elif shape == "triangle":
        b = int(input('base: '))
        h = int(input('height: '))
        area = 1 / 2 * b * h
    elif shape == "circle":
        r = int(input('radius: '))
        area = 3.14159 * r**2
    else:
        print('Print rectangle or triangle or circle')
        return
    print(f'Area: {area}')