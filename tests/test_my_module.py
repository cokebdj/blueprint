from my_module.my_module import square

import pytest

def test_square_gives_correct_value(input_value):
    subject = square(input_value)
    assert subject == 16 

@pytest.mark.parametrize('inputs', [2,3,4])
def test_square_return_value_type_is_int(inputs):
    subject = square(inputs)
    assert isinstance(subject, int)