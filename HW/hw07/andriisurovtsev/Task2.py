def area_of():
    area = int(input("Введить:\n1 - якщо це площа прямокутника\n2 - якщо це площа трикутника\n3 - якщо це площа кола\n"))
    if area == 1:
        length = float(input("Введіть довжину: "))
        width = float(input("Введіть ширину: "))
        area_of_rect = length * width
        print("Площа прямокутника: ", area_of_rect)
    elif area == 2:
        base = float(input("Введіть основу: "))
        height = float(input("Введіть висоту: "))
        area_of_tria = 0.5 * base * height
        print("Площа трикутника: ", area_of_tria)
    else:
        pi = 3.14
        radius = float(input("Введіть радіус: "))
        area_of_circ = pi * (radius ** 2)
        print("Площа кола: ", area_of_circ)
area_of()