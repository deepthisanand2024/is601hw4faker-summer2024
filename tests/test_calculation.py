''' This module contains tests for the calculator operations and Calculation class.'''

# Import statements:
# Disable specific pylint warnings that are not relevant for this test file.
# Import the Decimal class for precise decimal arithmetic, which is especially
# useful in financial calculations.
# Import pytest for writing test cases.
# Import the Calculation class from the calculator package to test its functionality.
# Import the arithmetic operation functions (add, subtract, multiply, divide) to be tested.
# pylint: disable=unnecessary-dunder-call, invalid-name, disable=line-too-long
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import divide

# pytest.mark.parametrize decorator is used to parameterize a test function, enabling it to be called
# with different sets of arguments. Here, it's used to test various scenarios of arithmetic operations
# with both integer and decimal operands to ensure the operations work correctly under different conditions.

def test_calculation_operations(a, b, operation, expected):
    """
    Test calculation operations with various scenarios.
    """
    calc = Calculation(a, b, operation)
    assert calc.getOutput() ==  expected, f"Failed {operation.__name__} operation with {a} and {b}"  # Perform the operation and assert that the result matches the expected value.

def test_divide_by_zero():
    """
    Test division by zero to ensure it raises a ValueError.
    
    This test checks that attempting to perform a division operation with a zero divisor
    correctly raises a ValueError, as dividing by zero is mathematically undefined and should be handled as an error.
    """
    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Error: Division by zero"): # Expect a ValueError to be raised.
        calc.getOutput() # Attempt to perform the calculation, which should trigger the ValueError.
