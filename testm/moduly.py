
def is_prime(number):
    for i in range(2, number // 2 + 2):
        if not number % i:
            return False
    return True