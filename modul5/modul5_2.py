my_list = [1, 2, 3]

my_list_iter = my_list.__iter__()
print(my_list_iter)
print(next(my_list_iter))
print(next(my_list_iter))


# print(len(my_list_iter))

# generator   obiect pe care se call-uie metode de tip next

def my_generator():  # construieste un obiect de tipul generator
    for i in range(3):
        print('before')
        yield i  # un fel de return ce nu incheie executia functiei
        print('after')


gen = my_generator()
print(type(gen))
print(gen.__next__())
print('Step 1')
print(gen.__next__())
print('Step 2')
print(gen.__next__())
print('Step 3')
# print(gen.__next__())
print()
# print(my_generator().__next__())

# list comprehension
my_list_c = [i for i in range(10)]
print(my_list_c)

my_gen = (i for i in range(3))
print(my_gen)
print(my_gen.__next__())
print(my_gen.__next__())
print(my_gen.__next__())
print()
print()


def generator_even_numbers(x):
    for i in range(x):
        if i % 2 == 0:
            print('Even number is: ')
            yield i


number = generator_even_numbers( 10)  # generatorul creeaza un obiect si este nevoie sa il retin intr-o variabila si pe el sa apelez next
print(number.__next__())
print(number.__next__())
print()

my_var = (i for i in range(5) if i % 2 != 0)   #generator for odd numbers
print(my_var.__next__())
print(my_var.__next__())

print()
print()

