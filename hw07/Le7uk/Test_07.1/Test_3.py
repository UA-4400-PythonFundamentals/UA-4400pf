def count_num_characters(a):
    """
    повертаєм відсортований словник - (c)

    """
    c = {}
    for i in a:
        if i in c:
            c[i] += 1
        else:
            c[i] = 1
    return c
print(count_num_characters("hello"))

