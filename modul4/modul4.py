# Dictionary

empty_dict = {}
print(empty_dict)
print(type(empty_dict))

dict_with_values = dict(a='a')
# dict_with_values = dict(1='a')
print(dict_with_values)

my_dict = {1: 'a', 2: 'b'}
print(my_dict)

my_dict = {1: 'a', 2: 'b', 1: 'c'}
print(my_dict)

list1 = [1, 2]
list2 = [1, 2, 3]
my_dict = {None: 'a', True: 'b'}
list1.append(3)

my_str = 'abc'
print(dir(my_str))
print(my_str.__hash__())
print('abc'.__hash__())
print(dir(list1))
print((1, 3, True).__hash__())
# print(list1.__hash__())

# muttable
new_dict = dict()
print(id(new_dict), new_dict)
new_dict.update({'a': 'b'})
print(id(new_dict), new_dict)

# methods
print()
keys = new_dict.keys()
print(type(keys), next(keys.__iter__()))
values = new_dict.values()
print(type(values), next(values.__iter__()))
items = new_dict.items()
print(type(items), next(items.__iter__()))

# unpack tuple

var1, var2, var3, *var4, var5 = (1, 2, 3, 4, 5, 6)
print(var1, var2, var3)
print(var4)
print(var5)

for x, y in [var4]:
    print(x, y)

# get method and []
print()
print(new_dict.get('a'))
print(new_dict['a'])
print(new_dict.get('b', 0))

# remove key
print()
new_dict.pop('a')
print(new_dict)

# exercise

mag1 = {'mere': 10, 'pere': 15, 'prune': 6, 'ananas': 20}
mag2 = {'mere': 11, 'pere': 15, 'prune': 6}
mag3 = {'mere': 10, 'pere': 16, 'prune': 7, 'papaya': 25}
lista_de_magazine = {'mag1': mag1, 'mag2': mag2, 'mag3': mag3}
lista_de_cumparaturi = {'mere': 2, 'pere': 3, 'prune': 6}


# def best_buy(shops, shopping_list):
def best_buy(shops, shopping_list):
    totals = {}
    result = None
    totalcost = None
    for product, nr_items in shopping_list.items():
        for shop_name, shop_items in shops.items():
            cost = shop_items[product] * nr_items
            print(f'In {shop_name} object {product} costs: ', cost)
            totals.update({shop_name: totals.get(shop_name, 0) + cost})

    print(totals)
    for key, value in totals.items():

        if (totalcost is None) or (value < totalcost):
            result = key
            totalcost = value
    return result


print(best_buy(shops=lista_de_magazine, shopping_list=lista_de_cumparaturi))


# find Prime number

def is_prime(number):
    return bool


# sets

my_set = set()
print(type(set), my_set)

my_set1 = {1, 2, 3, 4, 5, 5}
print(type(set), my_set)

my_set2 = {5, 3, 1}
my_set2.update({7})
print(my_set2)

print(my_set2.pop())

print(my_set2.difference(my_set1))
print(my_set1.difference(my_set2))
print(my_set2.intersection(my_set1))
print(my_set1.intersection(my_set2))

print(my_set1)
print(my_set2)
print(my_set2.symmetric_difference(my_set1))
print(my_set1.symmetric_difference(my_set2))
print()
print(my_set2.union(my_set1))
print(my_set1.union(my_set2))


test_data = [[1,2,3], [3,3,5], [8,9,4]]
def pinball_game_test(game_data, ful_range=10):
    range_values = set(range(1, ful_range + 1))
    ful_set = set()
    for mach_game in game_data:
        ful_set = ful_set.union(mach_game)
    return range_values.difference(ful_set)

print(pinball_game_test(test_data))