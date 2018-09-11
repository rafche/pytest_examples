import random
import pytest

from some_funcs import square, multiply, sumlist, cutlastelement, print_statement


class TestClass(object):

    @pytest.mark.multiply
    def test_multiply(self):
        '''
        test multiply funciton with hardcoded results
        :return: just assert statements
        '''
        assert multiply(1, 2)
        assert multiply(3, 4) == 12
        assert multiply(2, 5) == 10
        assert multiply(3, 5) == 15
        assert multiply(3, 5) == 3 * 5

    @pytest.mark.square
    def test_square(self):
        '''
        test square funciton with one hardcoded resulst
        :return: just assert statements
        '''
        assert square(5) == 25

    @pytest.mark.sumlist
    def test_sumlist(self):
        '''
        test with dynamic functions
        :return: just asserting
        '''
        rand_list = [random.randrange(1, 101, 1) for _ in range(10)]
        assert sum(rand_list) == sumlist(rand_list)

    @pytest.mark.cutlastelement
    def test_cutlastelement(self):
        '''
        test cutlastelement
        :return: just some asserting
        '''
        rand_list = [random.randrange(1, 101, 1) for _ in range(10)]
        assert cutlastelement(rand_list) == rand_list[:-1]

    @pytest.mark.print_statement
    def test_print_statement(self):
        '''
        test printstatement
        :return:
        '''
        assert print_statement('some string')


