def day_of_the_week(num: int):
    if not (1 <= num <= 7):
        raise ValueError('Out of range')

    days = {
        1: 'Monday',
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday ",
        7: "Sunday"
    }
    return days[num]



if __name__ == "__main__":
    try:
        num = int(input('Enter number: '))
        day = day_of_the_week(num)
        print(day)
    except ValueError as e:
        print(e)

