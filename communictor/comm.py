"""Documentation on module"""
from utils import generate_primes
from random import randint


class Client():
    '''
    Documentation on class
    '''
    def __init__(self, base, key):
        """
        Documentation on function
        :param base:
        :param key:
        """
        self.base = base
        self.key = key

    def _prime(self):
        prime_nr = [i for i in generate_primes(256) if i >= 129]
        random_nr = randint(0, len(prime_nr) - 1)
        self.prime = prime_nr[random_nr]
        return self.prime

    def generate_local_secret(self):
        self.secret = randint(129, self.prime)
        self.local = pow(self.secret, self.base) % self.prime

    def get_secret(self, secret):
        self.secret1 = pow(self.base, secret) % self.prime


class Server():
    def __init__(self, base, key):
        self.base = base
        self.key = key

    def get_prime(self, prime):
        self.prime = prime

    def generate_local_secret(self):
        self.secret = randint(129, self.prime)
        self.local = pow(self.secret, self.base) % self.prime


    def get_secret(self, secret):
        self.secret1 = pow(self.secret, secret) % self.prime
