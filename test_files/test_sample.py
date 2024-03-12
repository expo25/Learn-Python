import pytest

class TestClassOne:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hi"
        assert hasattr(x, "hi")

class TestClassTwo:
    @staticmethod    
    def func(x):
        return x + 1

    def test_answer(self):
        assert self.func(3) == 5
        
class TestClassThree:
    value = 0
    
    def test_three(self):
        self.value = 1
        assert self.value == 1
        
    def test_four(self):
        assert self.value == 1