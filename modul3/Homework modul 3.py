""" Homework 3  - needs to be presented before exam day"""


# 25P
# Write a function that takes in a list of objects and converts each object in the list into a int.
# For objects that can't be directly converted to int should have there length counted
# The function will return a list with a int values ordered from largest to smallest.
# example [1, True, '123', False, 6, ()] will be transformed into [123, 6, 1, 1, 0, 0]

def ordered_ints(list_of_objects: list):
    new_list = []
    for i in list_of_objects:
        if i == ():
            new_list.append(int(len(i)))
        else:
            new_list.append(int(i))
    new_list.sort(reverse=True)
    return new_list


print(ordered_ints([1, True, '123', False, 6, ()]))


# 25P - (do not rush to resolve this)
# For recursive functions try reading the articles below if you find need more information
# https://realpython.com/python-thinking-recursively/
# https://www.python-course.eu/python3_recursive_functions.php
# After reading the above articles try creating a function to calculate the series (1^2)+(2^2)+(3^2)...(n^2)
# The function will receive an int that indicate the number of iterations, or how many times we have (x^2)+
# when resolving try using this logic: 1^2+2^2 is 1^2+(1^2+1^2)^2

def sum_of_square(n: int):
    if n == 0:
        return 0
    else:
        return n ** 2 + sum_of_square(n - 1)


print(sum_of_square(10))


# 25P
# Write a function that will calculate factorial of numbers squared.
# For n = 3 the function should calculate (1^2)*(2^2)*(3^2)

def factorial_of_squares(n: int):
    if n == 1:
        return 1
    else:
        return n ** 2 * factorial_of_squares(n - 1)


print(factorial_of_squares(3))


# 25P
# Write a function that takes in a string as argument and returns a tuple after performing the following actions:
# - the string is split after the first encountered space.
# - all letters in the first half will be transformed to upper case letters
# - all characters that are not lower case letters in the second half will be replaced with "_"
# - returned tuple contains the two processed strings
# example: "1234567a Text to te5t" will become  ("1234567A", "_ext_to_te_t")

def process_text(text: str):
    first_text = ""
    second_text = ""
    for i in text:
        if i == " ":
            split_text = text.split(" ", 1)[0]
            first_text = split_text.upper()

            for i in text.strip(split_text):
                if i != i.lower() and i != " ":
                    i = "_"
                    second_text += i
                else:
                    second_text += i

    return (first_text, second_text)


print(process_text('1234567a Text to te5t'))
