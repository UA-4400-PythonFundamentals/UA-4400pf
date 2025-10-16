def numberOfCharacters(str):
    test = {}
    for i in str:
        test.update({i: str.count(i)})
    return test
