# You can test repeat you code to see in different system.

'''
from string import digits
from itertools import product

for code in product(digits, repeat=6):
    print("".join(code))

'''

'''

from string import ascii_letters
from itertools import product

for code in product(ascii_letters, repeat=6):
    print("".join(code))

'''

'''
from string import ascii_letters, digits, punctuation
from itertools import product

for code in product(ascii_letters + digits + punctuation, repeat=6):
    print("".join(code))

'''
