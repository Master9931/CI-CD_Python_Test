import pytest
from calculator import add, divide


def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0


def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(1, 0)