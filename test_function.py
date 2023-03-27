from function import validate_number_egg
import pytest

@pytest.mark.validate  
def test_input_1():
    input_number_egg = 1
    expected_result = 4
    actual_result = validate_number_egg(input_number_egg)
    assert expected_result == actual_result

@pytest.mark.validate  
def test_input_12():
    input_number_egg = 12
    expected_result = "36"
    actual_result = validate_number_egg(input_number_egg)
    assert expected_result == actual_result

@pytest.mark.validate  
def test_input_60():
    input_number_egg = 60
    expected_result = "2100"
    actual_result = validate_number_egg(input_number_egg)
    assert expected_result == actual_result

@pytest.mark.validate 
def test_out_of_range_input_0_5():
    input_number_egg = 0.5
    expected_result = "out of range"
    actual_result = validate_number_egg(input_number_egg)
    assert expected_result == actual_result

@pytest.mark.validate 
def test_out_of_range_input_minus_1_5():
    input_number_egg = -1.5
    expected_result = "out of range"
    actual_result = validate_number_egg(input_number_egg)
    assert expected_result == actual_result

@pytest.mark.validate 
def test_input_integer_input_1_5():
    input_number_egg = 1.5
    expected_result = "input integer"
    actual_result = validate_number_egg(input_number_egg)
    assert expected_result == actual_result
