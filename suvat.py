class Suvat:
    def __init__(self, **suvat):

        # define filter
        valid_keys = ['s','u','v','a','t']

        # initial check to make sure all keys present
        for key in suvat.items():
            if key not in valid_keys:
                raise TypeError('Invalid suvat key') # do something with keys here.
Suvat(s = 3, u = 3, k =4)
        