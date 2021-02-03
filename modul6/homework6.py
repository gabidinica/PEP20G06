""" Homework 6 - needs to be presented before exam day
A car factory requires a class for an iterable object that can be used to keep track of car serial and lot numbers
produced in a certain day. A instance variable called "day" will record the date, in any format/value you prefer.

Lot number and serial number had values of 0 and 0 respectively for the first car produced.

Serial number is incremented with each car produced, lot number is incremented every 20 cars produced.

Each instance of the class will get constructor arguments the starting serial and number of cars produced for that day.

Your instance will need to calculate the lot numbers and serials produced in that specific day.
ex: Instance has start serial 30 and number of cars produced is 30 meaning resulting in serial numbers produced that day
are: 30, 31 ..59, 60 and lot numbers produced that day are 1, 2, 3 (serial 60 is part of lot 3)

Cars with odd serial number are right side driving cars and the cars with even serial number are left side driving cars.
Your instance will have methods for returning serial numbers for right side driving cars and left side driving cars.
Iterating the object will return the lot numbers produced that day

1) Implementation:
    a) Correct implementation of iterable object. 10P
    b) Correct implementation of iterator object. 10P
    c) Correct implementation of methods returning right and left side driving cars. 20P
2) Execution:
    a) Create object from class defined above using start serial 111 and number of cars produced 91. 10P
    b) Print all left hand and right hand serials for the object above: 10P
    c) Iterate the object created above and write the lot numbers on new lines in a file. 20P
3) Document:
   a) Add type hints for all arguments 5P
   a) Add module documentation 5P
   b) Add document all classes 5P
   c) Add document all methods 5P
"""

"""Creating the car factory classes using a class for iterator and a class for object"""

from datetime import datetime


class CarFactoryIterator:
    """The class for iterating cars """

    def __init__(self, lot):
        self.lot = lot

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.lot) == 0:
            raise StopIteration
        return self.lot.pop(0)


class CarFactory:
    """ The class for iterating the cars  """

    def __init__(self, cars_number: int, serial_number: int):
        self.serial_l = []
        self.lot_l = []
        self.day = datetime.now()
        self.serial_l.append(serial_number)
        self.lot_number = serial_number // 20
        for i in range(1, cars_number + 1):
            self.serial_l.append(serial_number + i)
        for j in range(1, cars_number + 2, 20):
            self.lot_number += 1
            self.lot_l.append(self.lot_number)

    def right_side_driving(self) -> list:
        list_right_side = []
        for i in self.serial_l:
            if i % 2 != 0:
                list_right_side.append(i)
        return list_right_side

    def left_side_driving(self):
        list_left_side = []
        for i in self.serial_l:
            if i % 2 != 0:
                list_left_side.append(i)
        return list_left_side

    def __iter__(self):
        return CarFactoryIterator(self.lot_l)


cars = CarFactory(111, 91)
print("Serial number list: ", cars.serial_l)
print("Lot car list: ", cars.lot_l)
print("driving on the right: ", cars.right_side_driving())
print("driving on the left: ", cars.left_side_driving())


f = open("homework6t.txt", "x")
for i in cars:
    f.write(str(i))
    f.write("\n")