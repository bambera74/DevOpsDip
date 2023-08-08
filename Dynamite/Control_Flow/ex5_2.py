def middle_of_string (my_string):
    length = len(my_string)
    print (length)
    if length % 2 == 0:
        print (None)
    else:
        print (my_string [length //2])

middle_of_string ('abcde')