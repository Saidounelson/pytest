import pytest
import time
import source.my_function as my_function


def test_add():
    result = my_function.add(number_one=1, number_two=4)
    assert result == 5

def test_add_strings():
    result = my_function.add(number_one="i like",number_two="burgers")
    assert result == "i like burgers"
def test_devide():
    result = my_function.devide(number_one=4, number_two=2)
    assert result == 2

# def test_devide_by_zero():
#     with pytest.raises(ValueError):
#         my_function.devide(number_one=10, number_two=0)
@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = my_function.devide(number_one=10, number_two=5)
    assert result == 2
    
@pytest.mark.skip(reason="This feature is corrently broken")
def test_add():
    assert my_function.add(number_one=1,number_two=2) == 3

@pytest.mark.xfail(reason="We know we cannot divide by zero")
def test_divide_zero_broken():
    my_function.devide(number_one=4,number_two=0)

