import pytest

class TestClassOne:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hi"
        assert hasattr(x, "upper")
        #To pass, the 2nd arg must contain an attribute of the string class in python.

class TestClassTwo:
    @staticmethod    
    def func(x):
        return x + 1

    def test_answer(self):
        assert self.func(3) == 4
        
class TestClassThree:
    value = 0
    
    def test_three(self):
        self.value = 1
        assert self.value == 1
        
    def test_four(self):
        assert self.value == 1
        # Example of a failure bc there is was no self.value declaration.
        
    def test_five(self):
        y = "string"
        xy = y.startswith("s")
        assert xy
        # attributes of string class practice 