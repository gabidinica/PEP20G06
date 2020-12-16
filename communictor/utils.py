def crypt_decrypt(string, key):
    result = []
    for letter in string:
        result.append(chr(ord(letter).__xor__(key)))
    return ''.join(result)


def is_prime(number):
    for i in range(2, number // 2 + 2):
        if not number % i:
            return False
    return True


def generate_primes(limit):
    result = []
    for i in range(limit):
        if is_prime(i):
            result.append(i)
    return result

print('name of module is:', __name__)
print('name of package is:',__package__)