# FOR loop

# Iterable object
string1 = 'My String'
print(dir(string1))

# Next for iterable objects
print(string1.__iter__())
print(dir(string1.__iter__()))
print()

iterator = string1.__iter__()
print(iterator.__next__())
print(iterator.__next__())
print()

# obiect neiterabil
int1 = 12345
print(dir(int1))
print()

my_int = 123
# for i in my_int:
#     print(i)

# obiecte booleene : nu sunt iterabile
my_bool = True
print(dir(my_bool))
print()

for i in 'my_text':
    print(i)
print('done')

# string compare
nr = ord('a')  # extrage numarul specific fiecarui caracter
print(f'Number of a: {nr}')

nr = ord('b')
print(f'Number of b: {nr}')

print('check if a == b:', 'a' == 'b')
print('check if a .__eq__(b):', 'a'.__eq__('b'))

print('check if a<=b', 'a' <= 'b')
print('check if a<=b', 'a'.__le__('b'))  # less or equal

print('check if a<b', 'a' < 'b')
print('check if a<b', 'a'.__lt__('b'))  # less than

print('check if a>b', 'a' > 'b')
print('check if a>b', 'a'.__gt__('b'))  # greater than
print()

print('check if a>=b', 'a' >= 'b')
print('check if a>=b', 'a'.__ge__('b'))  # greater or equal than
print()

print(dir(1))
print('1+2=', (1).__add__(2), '\n')

# exercise exit for on _
for i in 'my_text':
    if '_' == i:
        break
    else:
        print(i)
print()

# exercise print 'yey' if _ not in text
var1 = ''
for i in 'mytext':
    if '_' == i:
        var1 = '_'
print('var1=', var1)
if var1 != '_':
    print('yey')
print()

# exercise print 'yey' if _ not in text
var1 = ''
for i in 'mytext':
    if '_' == i:
        var1 = '_'
else:
    print('yey')
print()

for i in 'my_text':
    if '_' == i:
        break
else:
    print('for else statement:', 'yey')
print()

# sum of all characters if it's not ' '
sum = 0
for i in 'My Text':
    if i != ' ':
        sum += ord(i)
    else:
        break
else:
    print(sum)

# print the last letter from text only if the next is greater than 3
text = 'My Text'
nr = 0
var1 = ''
for i in text:
    nr += 1
    if nr > 3:
        var1 = i
else:
    print(var1)
print()

# len function
print(len('my_text'))
print('my_text'.__len__())

text = 'my_text'
if len(text) > 3:
    for i in text:
        var = i
    print(i)

# continue

# new text without spaces
text = 'my text'
new_text = ''
for letter in text:
    if letter == ' ':
        continue
    new_text = new_text + letter
print(new_text)
print()

# text add just letter with number <= 100
text = 'my text'
new_text = ''
for letter in text:
    if ord(letter) <= 100:
        continue
    new_text = new_text + letter
print(new_text)
print()

# WHILE loop
# a = 3
# while a > 2:
#     if a > 2:
#         a = a - 1
#     else:
#         a = a + 1
#     print('True')

# Read while value is smaller than 100
# my_bool = True
# while my_bool:
#     nr = int(input())
#     print(nr)
#     if nr > 100:
#         my_bool = False

# len(text)<5 letters then add new characters
my_text = 'my_text'
new_text = ''
var1 = 0
while len(new_text) < 5:
    new_text = new_text + my_text[var1]
    var1 += 1
    print(new_text)

# function range
range_object = range(3)
print(type(range_object))
range_iter = range_object.__iter__()
print(next(range_iter))
print(next(range_iter))
print(next(range_iter))

for i in range(3):
    print('in for:', i)

for i in range(2, 6, 2):
    print('in for:', i)

for i in range(2, 6):
    print('in for:', i)

# assigment operator
var1 = 1
print(var1)
var1 += 1  # var1=var1+1
print(var1)

var1 *= 3
print(var1)

var1 **= 3
print(var1)


