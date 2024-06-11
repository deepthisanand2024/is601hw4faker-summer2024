'''
This Python code defines a Calculator class that provides a simple interface for performing arithmetic operations (addition, subtraction, multiplication, division) on Decimal numbers. The class uses static methods, demonstrating a functional approach within an object-oriented context. 
Each operation method creates a Calculation object, performs the calculation, adds it to a history of calculations, and then returns the result. 
'''

''' Import statements '''
from calculator.calculationLogic import calculationLogic  # Manages history of calculations
from calculator.operations import add, subtract, multiply, divide  # Arithmetic operations
from calculator.calculation import Calculation  # Represents a single calculation
from decimal import Decimal  # For high-precision arithmetic
from typing import Callable  # For type hinting callable objects

''' Define Calculator class '''
class Calculator:
    @staticmethod
    def initCalc(x:Decimal, y:Decimal, operation:Callable[[Decimal, Decimal], Decimal]) ->Decimal:
        #This method will initiate the Calculation and return the result of calc
        cal = Calculation.createCalc(x, y, operation)
        calculationLogic.addHistory(Calculation)
        # Perform the calculation and return the result
        return cal.getOutput()
        
    
    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        # Perform addition by delegating to the _perform_operation method with the add operation
        return Calculator.initCalc(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        # Perform subtraction by delegating to the _perform_operation method with the subtract operation
        return Calculator.initCalc(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        # Perform multiplication by delegating to the _perform_operation method with the multiply operation
        return Calculator.initCalc(a, b, multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        # Perform division by delegating to the _perform_operation method with the divide operation
        return Calculator.initCalc(a, b, divide)
    