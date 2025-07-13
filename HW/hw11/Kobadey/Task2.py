def check_day(day):
    try:
        days = {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 7:"Sunday"}
        day = int(day)
        if day < 1 or day > 7:
            raise TypeError
        return f"Today is {days[day]}"
    except ValueError:
        return "A day must be an integer"
    except TypeError:
        return "A day must be between 1 and 7"
day = input("Enter a day: ")
print(check_day(day))


