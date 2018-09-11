import pandas as pd


def multiply(x, y):
    '''
    multiply x * y
    :param x:
    :param y:
    :return: result of multiplication
    '''
    return x * y


def square(x):
    '''
    build square
    :param x:
    :return:
    '''
    return x * x


def sumlist(x_list : list):
    '''
    create sum of elements of list
    :param x_list: list with int / float
    :return: sum of list
    '''
    return sum(x_list)


def cutlastelement(x_list : list):
    '''
    return list without last element
    :param x_list:
    :return:
    '''
    return x_list[:-1]


def print_statement(x_string):
    '''
    print input string
    :return: True 
    '''
    print(x_string)
    return True
 

if __name__ == '__main__':
    print(multiply(3, 4))
    print(square(2))
    print(sumlist([1, 2, 4, 4, 5]))
    print(cutlastelement([1, 2, 3, 4]))
    print(print_statement('some_serious_string'))
