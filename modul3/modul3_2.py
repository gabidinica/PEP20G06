# Functions

def my_print(value):
    print(type(value))
    print(value)


my_print('Hello world')
print('x')


# multiple arguments
def my_print(value, value2, value3):
    print(type(value))
    print(value, value2, value3)


my_print('Hello world', 'x', 'y')
print()


def my_print(*args, end='\n'):
    print(type(args))
    print(type(end))
    print(*args, end=end)


my_print('Hello world', 'x', 'y', end='$\n')
print()


def my_print(*args, **kwargs):  # keyword args
    print(type(args))
    print(type(kwargs))
    print(*args, **kwargs)


my_print('Hello world', 'x', 'y', end='\n', sep='_')
print()


# def my_input():
#     my_val = input("Insert string: ")
#     print(my_val)
#
#
# my_input()
# print()


# return
def add_numbers(nr1, nr2):
    result = nr1 + nr2
    print(result)
    return result


sum = add_numbers(1, 2)
print(type(sum))
print(sum)
print()


def pow_numbers(nr1, nr2):
    return nr1 ** nr2


pow_result = pow_numbers(2, 3)
print(pow_result)
print()

# Function object

print(add_numbers)
print(dir(add_numbers))  # returns methods
print(add_numbers.__call__(1, 2))
print()

for i in range(3):
    def add_numbers(nr1, nr2):
        result = nr1 + nr2
        print(result)
        return result


    print(add_numbers)
print()


# nested functions
def outside(number):
    def inside():
        return number + 1

    return inside


var1 = outside(10)
print(type(var1))
print(var1())
print()

number2 = 10


def outside(number):
    def inside():
        return number + number2

    return inside


var1 = outside(10)
print(type(var1))
print(var1())
number2 = 11
print(var1())
print()


# returns as many functions as many arg in initial function
def func1(*args):
    list1 = []
    for i in args:
        def intcn():
            print(i)

        list1.append(intcn)
    return list1


var1 = func1('a', 'b', 'c')
print(var1)

# lists

empty_list = []
print(empty_list)
print(dir(empty_list))
var1 = 3

empty_list = list()
print(id(empty_list))
empty_list.append(1)
print(empty_list)
empty_list.append(True)
print(empty_list)
print(id(empty_list))
empty_list.append(var1)
print(empty_list)
print(id(empty_list))
var1 = 4
print(empty_list)
print(id(empty_list))

print()
my_list_outside = []
my_list_outside.append(1)
my_list_inside = []
my_list_outside.append(my_list_inside)
my_list_inside.append(2)
print(my_list_outside)
my_list_inside.append(3)
print(my_list_outside)

# tuple
print()
empty_tuple = tuple()
one_object_tuple = (1,)
two_object_tuple = (1, 'a')
no_brackets_tuple = 1, 'a', True
print(type(no_brackets_tuple))
print(no_brackets_tuple)
new_two_object_tuple = (1, 'a')
new_two_object_tuple += None,
print(new_two_object_tuple)
print(id(two_object_tuple), id(new_two_object_tuple))

# Bit operations
result = 1 and 0 # classical
print(result)
result = 1 & 0 # bit
print(result)

result = 2 and 3 # classical
print(result)
result = 2 & 3 # bit
print(result)

result = 3 and -1 # classical
print(result)
result = 3 & -1 # bit
print(result)

print(-1 ^ 3)
print((-1).__xor__(3))

print(3 | 4)
print(~3)