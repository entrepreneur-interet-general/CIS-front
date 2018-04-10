
import string
import random

# from : https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python 
def pwd_generator( size=16, chars=string.ascii_uppercase + string.digits):
    """
    create a random password
    """
    return ''.join(random.choice(chars) for _ in range(size))