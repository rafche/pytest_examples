from some_funcs import power2
from some_funcs import multiply


class TestClass(object):

    def test_multiply(self):
        assert multiply(1, 2)
        assert multiply(3, 4) == 12
        assert multiply(2, 5) == 10
        assert multiply(3, 5) == 15

    def test_power2(self):
        assert power2(5) == 25


