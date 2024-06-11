'''Testing Operations'''
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import divide


def test_operation(a, b, operation, expected):
    '''Testing various operations'''
    calculation = Calculation(a, b, operation)
    assert calculation.getOutput() == expected, f"{operation.__name__} operation failed"

def test_divide_by_zero():
    '''Testing the divide by zero exception'''
    with pytest.raises(ValueError, match="Error: Division by zero"):
        calculation = Calculation(Decimal('10'), Decimal('0'), divide)
        calculation.getOutput()
        