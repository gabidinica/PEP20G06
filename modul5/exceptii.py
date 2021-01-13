# exceptii

# from time import sleep
#
# var=2
#
# try:
#     sleep(3)
#     result1 = 2 / var
#     if var==0:
#         result2 = 2 / '0'
# except ZeroDivisionError:               # doar in cazul acestei impartiri va fi printat mesajul
#     print('Bad division')
# except TypeError:                       #copiii lui Exception
#     print('Bad operand type')
# except Exception:                      #Keyboard Interrupt nu face parte din parintele Exception
#     print('something is wrong')
# else:
#     print('THis will only execute if no exception')
# finally:                                    #se executa indiferent de ce se intampla in cod
#     print('this will always be executed')

# function input si daca fct primeste orice altceva decat un numar ne da mesaj si daca primeste un nr imparte la 2

# def div():
#     var1 = input("Give number: ")
#     try:
#       return int(var1)/2
#
#     except ValueError:
#         print('Wrong var type')
#     except TypeError:
#         print('Wrong var type')
#
# print(div())


# def check_if_not_zero(nr=0):
#     if nr == 0:
#         raise ValueError('Number is 0')
#     print('value is not 0')
#     if nr==10:
#         raise ValueError('Different message')
#
# check_if_not_zero(nr=1)
# print('new call')
# try:
#     check_if_not_zero(nr=10)
# except ValueError as e:  # am salvat eroarea intr-un obiect
#     print("I will try again")
#     if e.args[0] == 'Number is 0':
#         print('This is my exception')
#     else:
#         raise e

# def div(divider=2):
#     if divider == 0:
#         raise AttributeError('nu e ok sa fie 0 ')
#     if divider % 2 == 1:
#         raise AttributeError('Not divisible with 2', 'Value 2 of Attribute Error')
#     var1 = input("Give number: ")
#     try:
#         return int(var1) / 2
#     except ValueError:
#         print('Wrong var type')
#     except TypeError:
#         print('Wrong var type')
#
#
# print(div())
# try:
#     div(3)
# except AttributeError as e:
#     print('Try again')
#     if e.args[0] == 'Not divisible with 2' and e.args[1] == 'Value 2 of Attribute Error':
#         print('This is my exception')


# CLASS


class CarFactory:
    model = "VW"
    counter = [0]

    # def number_of_cars(self):
    #     self.counter.append(self.counter.pop(0)+1)

    def __init__(self, color):  # constructor
        print('Building car')
        self.color = color
        self.counter.append(self.counter.pop(0) + 1)

    def __le__(self, second_car):
        print('first object is', self)
        print('second object is', second_car)
        return id(self) <= id(second_car)


# print('class attribute', CarFactory.model)  # specific clasei, cand nu este un obiect creat de clasa
# car1 = CarFactory('green')
# # print(car1.color)
# # print('Instance variable', car1.model)
# car2 = CarFactory('blue')
# # print(car2.color)
# # print('Instance variable', car2.model)
# print(CarFactory.counter)

#
# print('CAR1 is: ', car1)
# print('CAR2 is: ', car2)
# print(dir(car1))
# print()
# print(car1 <= car2)
# print(car2 <= car1)
# # print(car1.__le__(car2))


# muttable class attributes

class A:
    muttable_obj = []

    def change_attr(self, value):
        self.muttable_obj.append(value)


# a = A()
# print(a.muttable_obj)
# a.change_attr(1)
# print(a.muttable_obj)
# print()
# b = A()
# print(b.muttable_obj)
# b.change_attr(2)
# print(b.muttable_obj)
# print()
#

class A:
    __attr0 = 'really hide'  # private
    _attr1 = 'hide'  # protected
    attr2 = 'do not hide'


a = A()


# print(a._A__attr0)
# print(a._attr1)
# print(a.attr2)

class Factory:
    __counter = [0]

    def __init__(self):
        print()
        self.__counter.append(self.__counter.pop(0) + 1)


first_car = Factory()
print(first_car._Factory__counter)
second_car = Factory()
print(Factory._Factory__counter)
