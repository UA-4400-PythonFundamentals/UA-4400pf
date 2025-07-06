#Task3. Write a function that calculates the number
#of characters included in given string
#input: "hello"
#output: {"h":1, "e":1,"l":2,"o":1}


#there is no rule for this task, so i decided that H and h are the same character
#this means that all string will be in lower case
def number_of_characters(st):

    # if the line below commented then h and H will be different
    st = st.lower()
    counter = {}
    for ch in st:
        counter[ch] = counter.get(ch, 0) + 1
    return counter

your_string = input("Input your string:  ")
print(number_of_characters(your_string))