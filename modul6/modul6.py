# iterators

class ListIterator:

    def __init__(self, my_list: list):
        self.my_list = my_list

    def __next__(self):
        if len(self.my_list) == 0:
            raise StopIteration
        return self.my_list.pop(0)

    def __iter__(self):
        return self


iterator = ListIterator([1, 2, 3])
for i in iterator:
    print('i:', i)


# print(iterator.__next__())
# print(iterator.my_list)
# print(iterator.__next__())
# print(iterator.my_list)
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.my_list)

class IntIterator:

    def __init__(self, numar: int):
        self.numar = numar

    def __iter__(self):
        return self

    def __next__(self):
        for i in range(self.numar + 1):
            yield i


# !!!!!!! la examen obiect iterator : 2clase clasa obiect si clasa iteratorului
#
# int_iterator = IntIterator(3)
# for i in int_iterator:
#     print('i', i)

class IntObject():
    def __init__(self, nr):
        self.nr = nr  # variabila de instanta

    def __iter__(self):
        return IntIterator(self.nr)


#
# int_object = IntObject(3)
# for i in int_object:
#     print(i)
print()


# lambda functions
def func1(a, b):
    return a + b


func2 = lambda a, b: a + b

func3 = lambda a, b: True
print(func3(2, 3))

func1 = lambda x: pow(x, 2)
print(func1(3))

print()


# map
def process_chr(char: str):
    return chr(ord(char) + 1)


text = 'my_test to process'
result = map(process_chr, text)
print(result)
print(dir(result))

for new_obj in result:
    print(new_obj)

print('#' * 80)
result = map(lambda char: chr(ord(char) + 1), text)

for new_obj in result:
    print(new_obj)

print('#' * 80)

# o mapare cu o lista ce contine 100 de numere si mapez nr respective la impartit la 2

my_list = [i for i in range(100)]
for i in map(lambda k: k / 2, my_list):
    print(i)

print()
print()

my_list = [i for i in range(100)]
for i in map(lambda k: pow(k, 2) % 2 == 0, my_list):
    print(i)

print()
print()

list_number = [i for i in range(10)]
result = map(lambda k: k if k % 2 == 0 else None, list_number)
for i in result:
    print(i)

print('#' * 80)

# filter
list_number = [i for i in range(10)]
result = filter(lambda a: a > 5,
                list_number)  # pentru un obiect din lista, conditia sa returneze True si trece de filtru
for i in result:
    print(i)
print()

# filtru caracter si fiecare caracter sa verifice daca e mai mare ca m
text = "".join([chr(i) for i in range(97, 123)])
result = filter(lambda a: a > 'm', text)
for i in result:
    print(i)

print('*' * 80)

text = "".join([chr(i) for i in range(97, 123)])
result = filter(lambda a: ord(a) + 1 > 100, text)
for i in result:
    print(i)
print('*' * 80)
# any                #daca un obiect ce a trecut de o mapare ce este adevarat atunci returneaza True

my_list = [1, 'a', True, False, False]
my_list_f = [0, "", None, False, False]
print(any(my_list))
print(any(my_list_f))

# all
print('*' * 80)
my_list = [1, 'a', True]
my_list_f = [1, 'a', True, False]

print(all(my_list))
print(all(my_list_f))


# mostenire

class Wolf():
    bark = True

    def hunt(self):
        print("hunting")
 #       raise NotImplemented

    def method_1(self):
        pass


class Dog(Wolf):

    def  hunt(self):
        print('can t do that')


    def method_2(self):
        pass


dog = Dog()
print('dog barks: ',dog.bark)
dog.method_2()
dog.method_1()
dog.hunt()