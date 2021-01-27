class Animal(object):
    def __init__(self, species):
        self.species = species

    def hunt(self, pray):
        print('nothing')


class Wolf(Animal):
    bark = True

    def __init__(self, species):
        super().__init__(species)
        self.attribute = "wild"

    def hunt(self):
        print("hunting")

    #       raise NotImplemented

    def method_1(self):
        pass


class Coyote(Animal):
    bark = True

    def __init__(self, species):
        super().__init__(species)
        self.attribute = "wild"

    def hunt(self):
        print("hunting=")

    #       raise NotImplemented

    def has_more_teeth(self):
        print("adding teeth")

    def method_1(self):
        pass


class Car():
    __key = 123510  # private
    _engine = 1.8  # protected

    def __init__(self, color):
        self.attribute = color
        self.__key = 78910
        self._engine = 2

    def start(self):
        self.__engine_code = 521
        print("start")


class Dog(Coyote, Wolf, Animal, Car):  # ordinea de mostenire: cei mai apropiati parinti, apoi bunicii
    def __init__(self, species):
        super().__init__(species)
        self.attribute = "domestic"

    # def hunt(self):
    #     print('can t do that')

    def method_2(self):
        pass


dog = Dog("dog")
print('dog barks: ', dog.bark)
dog.method_2()
dog.method_1()
dog.hunt()
print(dog.attribute)
dog.has_more_teeth()
dog.start()


class Suv(Car):
    def __init__(self, size, color):
        super(Suv, self).__init__(color)
        self.size = size
        self._Car__key = 435678
        self._engine = 3

    def all_wheel_drive(self):
        print("all wheel drive active")


suv = Suv(12, "green")
print(suv._Car__key)
print(suv._engine)
suv.start()
print(suv._Car__engine_code)
suv._Car__engine_code = 20
print(suv._Car__engine_code)
print(80 * '*')

# file operations
from time import sleep


# open('C:\Users\dinic\PycharmProjects\PEP20G06\modul6\my_text')
# file = open('my_text', 'w')
# file.write('new text')
# file.close()
# # print(type(file))
# sleep(3)
#
# with open('my_text', 'w') as file2:
#     file2.write('new text2')

import logging

class FileWriter():

    def __init__(self, file_path):
        self.file_path = file_path

    def __enter__(self):
        self.file = open(self.file_path, 'x')  # creaza fisier
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.write('\n')
        self.file.write(str(exc_tb.tb_frame).split(',',1)[1])
        self.file.close()
        return True



with FileWriter('new_file') as file:
    my_string = int(input(">>>"))
    while my_string:
        my_string2 = input("...")
        file.write(str(my_string) + ("\n" if my_string2 else ""))
        my_string = int(my_string2)


