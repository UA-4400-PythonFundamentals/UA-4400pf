def solution(number):
    if number < 0 :
        return 0
    else:
        sum = 0
        for i in range(number):
            if i % 3 == 0:
                sum +=i
                continue
            elif i % 5 == 0:
                sum +=i
        return sum