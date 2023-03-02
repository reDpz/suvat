import numpy
class Suvat:
    def __init__(self, *, s=None, u=None, v=None, a=None, t=None):
        i = 0
        self.suvat = {
            's':s,
            'u':u,
            'v':v,
            'a':a,
            't':t
            }
        
        # switch case to find each letter.
        self.switch_case = {
            's':self.find_s,
            'u':self.find_u,
            'v':self.find_v,
            'a':self.find_a,
            't':self.find_t
        }
        for index in self.suvat:
            if index == None:
                i +=1
        if i>2:
            # dont do anything if theres less than 3 known values
            print('Not enough suvat values')
        else:
            self.present()
            for key in self.suvat:
                if key not in self.present_keys:
                    self.find(key)
        
    # take input and redirect to correct
    def find(self, letter):
        return self.switch_case.get(letter, print('Invalid key.'))()
    
    # make sure it's possibly to find said letter
    def valid(self, letter):
        if not letter in self.suvat:
            return False
        
    # check what keys have values and assign them to self.present
    def present(self):
        self.present_keys = []
        for key, value in self.suvat.items():
            if value != None:
                self.present_keys.append(key)
    
    # find displacement
    def find_s(self, number):
        pass # i'm lazy i'll do this later maybe sunday

Suvat(s = 2, v = 3, t = 3)