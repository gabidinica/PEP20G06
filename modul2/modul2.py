# binary numbers
# 1= 0b0001  ;   2 = 0b0010  ;  3=0b0011  ;   4= 0b0100   ; 5= 0b0101

# octal numbers
# 1= 0o0001   ; 2=0o0002 ; 8 = 0o0010 ; 9=0o0011

# hexadecimal numbers
# 1=0x00001   ; 2=0x0002 ; 9=0x0009 ; 10=0x000a   ; 11=0x000b  ; 15 =0x000f  ; 16=0x0010

# Print in base 2
print(0b0100)

# Print in baza 8
print(0o17)  # numarul 15
print(0o024)  # numarul 20

# Print in baza 16
print(0x11)  # numarul 17

# Arithmetic Operations
number1 = 3
number2 = 4
number3 = -3
print('division 3/4:', number1 / number2)
print('floordiv 4//3:', number2 // number1)
print('remainder 3%4:', number1 % number2)
print('negative 3:', -number1)
print('zero:', number1 + number3)
print('3 to the power of 4:', number1 ** number2)

a = 3
b = 4
c = 5
result = (-b + ((b ** 2) - 4 * a * c) ** (1 / 2)) / (2 * a)
print(result)
result2 = print((-b + pow((b ** 2) - 4 * a * c, 1 / 2)) / (2 * a))

number4 = 0.75
print('Type of number 0.75:', type(number4))
print('Type of number -3:', type(number3))
print('Type of results:', type(result))

number5 = 1.2 + 2.3j
print('Type of number 1.2 + 2.3j:', type(number5))

print('\n\n')

# String
string1 = 'Hello World'
string1 = "Hello World"
string1 = '''Hello World'''
string1 = """Hello World"""

# String interpretation
string5 = u'Hello\n World'  # format unicode
print(string5)
string5 = r'Hello\n World'  # format raw
print(string5)
string5 = f'Hello World: {string1}'  # string formatabil
print(string5)

# String Slices
result = string5[4]
print('Forth character is:', result)
result = string5[-3]
print('Third char from right is:', result)
result = string5[4:7]
print('4 to 7 char are:', result)
result = string5[9:4:-1]
print('Forth to ninth char is:', result)
result = string5[-2:-6:-1]
print(result)
result = string5[-2:-7:-2]
print('result:', result)

# Dot notation for strings:
print('string actions:', dir(string1))
print(string1.lower())
print(string1.upper())
print(string1.capitalize())
string1 = string1 + '{}{}'
print(string1.format(6, 'abcd'))
print(string1.find('ll'))
print(string1.center(20, '#'))  # stringul va ramane in centrul caracterelor

# Dot notation for ints:

print(number1.__add__(number2))
print((3).__add__(4))

print('multiplication: ', number1.__mul__(number2))
print('division:', number1.__truediv__(number2))
print('power of:', number1.__pow__(number2), number1 ** number2)
print('\n\n\n')

# Input function
# print('Your name is:',input('Enter text:'))
# my_name=input('Your last name:')
# print('Your last name is: ', my_name)

# number1=input('first number:')
# number2=input('second number:')
# print('sum is:', number1+number2)

# Casting
# print('Type of number1: ',type(number1))
# number1= int(number1)
# print('Type of number1: ',type(number1))
# number2 =int(number2)
# print('sum is:', number1+number2)

# number1 = 2
# number2 = 3
# print('Type of number1: ', type(number1))
# number1 = str(number1)
# print('Type of number1: ', type(number1))
# number2 = str(number2)
# print('sum is:', number1 + number2)
# print('\n\n\n')

# catena1=input('Catena1 in cm:')
# catena2=input('Catena2 in cm:')
# catena1=int(catena1)
# catena2=int(catena2)
# print('Area is:', (catena1*catena2)/2)

# Booleans
true1 = True
print(id(true1))
true2 = True
print(id(true2))

# Binary operations
# AND Operation
result = True and True
# print('Response type: ', type(result), result)
# OR Operation
# result = False or False
# print('Response type:', type(result), result)

# XOR Operation
# print('Bool operations:', dir(True))
# print('True xor False:', True.__xor__(False))

# Unary operations: NOT Operation applicable to a boolean object
# result = not True
# print('Not True is:', result)
# print('Not result is:', not result)

# Order of operations
print(not False and True)
print((not False) and True)
print(not (False and True))

# and
print((not False) and (not False))
print(not (not (False and False)))
print('Correct result:', not False and not False)

# Homework
print((True and True) or (False and False))
print()

# Cast
print('String bool:', str(True))
print('Integer bool True:', int(True))
print('Integer bool False:', int(False))
print('String "false" to bool:', bool(
    'false'))  # orice string ce nu este gol va fi transformat intr-un boolean de tip true, iar stringul gol va fi false
print('String "" to bool:', bool(''))
print('Int "100" to bool:', int(100))
print('Int "0" to bool:', int(0))

# Length of object
# print('len of "text"', len('text'))
# print('len of ""', len(''))
# print()

# Add bool objects
print('True + True + True =', True + True + True)
print('True - True - True =', True + True + True)

# None object
none = None
print('id:', id(none), id(None))  # None is saved only once in the memory
print('Actions for None:', dir(None))
print('\n\n')

# Aplicatii

string1 = 'Text to scramble'
print('initial string:', string1)
# Rearange odd letters:
# string1= string1[0::2]+string1[1::2]
# print('rearranged string:', string1)


# string1=string1[::-1]
# print('rearranged string:', string1)

# string1=string1[0::3]+string1[1::3]+string1[2::3]
# print('rearranged string:', string1)

string1 = string1[-1::-2] + string1[-2::-2]
print('rearranged string:', string1)

string1 = '^'
print(string1.center(8, '_'))
print('\n\n')

string1 = '--'
print(string1.center(6, '_'))
string1 = '| |'
print(string1.center(7, '_'))
string1 = '--'
print(string1.center(6, '_'))
print()

# if statement:
bool(True) == True

# comparation
print('Result of comp 1 with 1:', 1 == 1)
print('Result of comp 1 < 1:', 1 < 1)
print('Result of comp 2 > 1:', 2 > 1)
print('Result of comp 1 >= 1:', 1 >= 1)
print('Result of comp 2 != 1:', 2 != 1)

#my_number = int(input('Give number:'))
#if my_number < 3:
#    print(f'Number {my_number} is smaller than 3')
#elif my_number>5:
#    print(f'Number {my_number} is grater than 3')
#else:
#    print(f'Number {my_number} is good')
#print('\n')

#for my_var in 'My text':
 #   print(my_var)


my_new_text=''
for my_var in 'text to scramble':
    my_new_text=my_var+my_new_text
    print(my_new_text)

print(my_new_text[::-1])