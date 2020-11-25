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

print('multiplication: ',number1.__mul__(number2))
print('division:',number1.__truediv__(number2))
print('power of:',number1.__pow__(number2), number1**number2)