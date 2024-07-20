# contains functional & non-functional unit tests for the previous method
from is_prime import is_prime


def test_true():
    assert is_prime(3) == True

def test_false():
    assert is_prime(10) == False

class TestClass:
    def test_t(self):
        assert is_prime(7) == True

    def test_t(self):
        assert is_prime(16) == False

