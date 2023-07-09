from calculator import square
import pytest


def test_square_for_positive_numbers():
    assert square(2) == 4
    assert square(3) == 9


def test_square_for_negative_numbers():
    assert square(-2) == 4
    assert square(-3) == 9


def test_square_for_zero():
    assert square(0) == 0


def test_square_with_string():
    with pytest.raises(TypeError):
        square("cat")
