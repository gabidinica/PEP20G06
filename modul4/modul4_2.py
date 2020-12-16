# sleep
import time

print(time)
print(time.time())
print(time.sleep(1))

from time import sleep

print("Sleeping one second")
sleep(1)


def sleep(seconds):
    print(f"do nothing for {seconds}")


# print(sleep(10))

from time import sleep as imported_sleep

print(imported_sleep)

# our module
import communictor

import sys

print(sys.path)

# add to path
sys.path.append('Users/dinic/PycharmProjects/PEP20G06')
print(sys.path)

# use communictor
print(communictor.VAR1)
print(communictor.is_prime(19))

# import modulm
import testm

print(testm.is_prime(2))

print()

import datetime
from time import sleep, time, strftime


def my_time_function():
    result = []
    time1 = str(datetime.time(14, 30, 22))
    time2 = strftime('%H:%M:%S')
    print(time2.split(':'))
    for i in range(3):
        result.append(str(int(time2.split(':')[i]) - int(time1.split(':')[i])))
    print(result)
    return ":".join(result)


print(my_time_function())

# from time import sleep, time, strftime

# print(time())
# print(strftime('%H:%M:%S'))
print()


# recursive functions : putem apela functia in interiorul functiei

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print(factorial(10))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(10))
print()

my_list = [[1, [2, [3]]], [4, [5, [6]]], [7, [8, [9]]]]
# my_list = [1,2,3,4,5,6,7,8,9]
print(isinstance(my_list, list))  # ii dam un obiect si clasa obiectului
print(type(my_list) == list)
print()


# l1=[1,2]
# l2=[3,4]
# print(l1+l2)

def flatten_list(list_to_flatten):
    result = []
    for inner_object in list_to_flatten:
        if isinstance(inner_object, int):
            result.append(inner_object)
        else:
            result += flatten_list(inner_object)
    return result


print(flatten_list(my_list))


def flatten_list_to_tuple(list_to_flatten):
    result = []
    for inner_object in list_to_flatten:
        if isinstance(inner_object, int):
            result.append(inner_object)
        else:
            result += list(flatten_list_to_tuple(inner_object))
    return tuple(result)


print(flatten_list_to_tuple(my_list))

print()

# variables (global, non-local, local)

VAR1 = 'my var to print'


def outer(arg1):
    global VAR1
    VAR1 = 'some new message'
    VAR2 = 'inside outer'
    print(outer.__name__, VAR1)

    def inner(arg2):
        VAR1 = 'ceva'
        nonlocal VAR2
        VAR2 = 'now in inner function'
        print(inner.__name__, VAR1)
        print(inner.__name__, VAR2)

    inner(10)
    print(outer.__name__, VAR2)
    return inner


x = outer(10)
print(__name__, VAR1)
VAR1 = 'my new var to print'
x(10)
print()


def conversation():
    name_ = ''

    def hello(name='sir'):
        nonlocal name_
        name_ = name
        name_ = input(f'hello {name}:')

    def question(q='question'):
        print(f'{name_}, {q}')

    hello()
    return question


object = conversation()
object('What is that?')
