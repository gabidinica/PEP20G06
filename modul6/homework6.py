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
    """ The class for iterating the cars  """

    def __init__(self, cars_number, serial_number):
        self.day = datetime.now()
        self.cars_number = cars_number
        self.serial_number = serial_number

    def calculate_serial_and_lot_number(self):
        self.serial_number = 0
        self.lot_number = 0
        self.serial_number = self.cars_number + 1
        if self.serial_number >= 1:
            self.lot_nr = self.serial_number // 20
        print("In day: ", self.day, "we\'ve build: ", self.serial_number, "which in lot means: ", self.lot_nr)

    def right_side_driving(self):
        return self.serial_number % 2 != 0

    def left_side_driving(self):
        return self.serial_number % 2 == 0

    def __iter__(self):
        return self

    def __next__(self):
        for i in range(self.lot_nr + 1):
            yield i


class CarFactoryObject:
    """The class for the object """

    def __init__(self, nr):
        self.nr = nr

    def __iter__(self):
        return CarFactoryIterator(self.nr)


carFactoryIterator = CarFactoryIterator(42, 30)
print(carFactoryIterator.calculate_serial_and_lot_number())
print(carFactoryIterator.right_side_driving())
print(carFactoryIterator.left_side_driving())
# int_iterator = CarFactoryIterator(20,30)
# for i in int_iterator:
#     print('i', i)
