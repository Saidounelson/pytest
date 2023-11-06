import pytest

import source.my_function as my_function


def test_add():
    result = my_function.add(number_one=1, number_two=4)
    assert result == 5


def test_devide():
    result = my_function.devide(number_one=4, number_two=2)
    assert result == 2

# def test_devide_by_zero():
#     with pytest.raises(ValueError):
#         result = my_function.devide(number_one=10, number_two=2)
        
