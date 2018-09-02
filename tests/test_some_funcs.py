import random

from some_funcs import square, multiply, sumlist


class TestClass(object):

    def test_multiply(self):
        '''
        test multiply funciton with hardcoded results
        :return: just assert statements
        '''
        assert multiply(1, 2)
        assert multiply(3, 4) == 12
        assert multiply(2, 5) == 10
        assert multiply(3, 5) == 15

    def test_square(self):
        '''
        test square funciton with one hardcoded resulst
        :return: just assert statements
        '''
        assert square(5) == 25

    def test_sumlist(self):
        '''
        test with dynamic functions
        :return: just asserting
        '''
        rand_list = [random.randrange(1, 101, 1) for _ in range(10)]
        assert sum(rand_list) == sumlist(rand_list)

