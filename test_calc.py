import pytest
from calc import *

def test_add_int():
    assert add(2, 3) == 5

def test_add_float():
    assert add(2.1, 3.1) == 5.2

# def test_diff():
#     assert diff(10, 5) == 2.0

def test_diff_zero():
    with pytest.raises(ValueError):
        div(5, 0)