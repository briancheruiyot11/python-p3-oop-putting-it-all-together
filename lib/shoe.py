#!/usr/bin/env python3

# Shoe class represents a shoe with a brand and size
class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        
    @property
    def brand(self):
        return self._brand
    @brand.setter 
    def brand(self, value):
        if not isinstance(value, str):
            print("brand must be a string")
        else:
            self._brand = value   
    @property
    def size(self):
        return self._size
    @size.setter 
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value
            
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
        