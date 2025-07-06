import modules.calculate_area as area

def get_positive_int(prompt):
    while True:
        value = input(prompt)
        if value.isdigit() and int(value) > 0:
            return int(value)
        print('Please enter a valid positive number.')

def main():
    menu = (
        '1 - Calculate area of Rectangle',
        '2 - Calculate area of Triangle',
        '3 - Calculate area of Circle',
        '4 - Exit'
    )
    print('\n'.join(menu))
    while True:
        choice = input('Enter choice: ')
        if not choice.isdigit():
            print('Please enter a valid number.')
            continue
        choice = int(choice)
        if choice == 1:
            width = get_positive_int('Enter width: ')
            height = get_positive_int('Enter height: ')
            print(f"Area of rectangle: {area.rectangle(width, height)}")
        elif choice == 2:
            base = get_positive_int('Enter base: ')
            height = get_positive_int('Enter height: ')
            print(f"Area of triangle: {area.triangle(base, height)}")
        elif choice == 3:
            radius = get_positive_int('Enter radius: ')
            print(f"Area of circle: {area.circle(radius)}")
        elif choice == 4:
            break
        else:
            print('Invalid input.')

if __name__ == "__main__":
    main()