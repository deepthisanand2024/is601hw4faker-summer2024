'''
    This code snippet demonstrates how to define a class in Python that 
    encapsulates a mathematical calculation, including two operands (a and b) 
    and an operation (like add or subtract). 
    The operation parameter is a higher-order function, meaning it takes 
    functions as arguments or returns them. 
    This approach leverages Python's first-class functions to create 4
    flexible and reusable code. The use of Decimal from the decimal 
    module instead of floating-point numbers is crucial for 
    financial and scientific calculations that require high precision. 
    The __repr__ method provides a developer-friendly string representation 
    of the object, useful for debugging and logging.
'''

''' Import statements'''
from decimal import Decimal
from typing import Callable
from calculator.operations import add, subtract, multiply, divide

# Definition of the Calculation class with type annotations
class Calculation:

    # Constructor with type hints for parameters and the return type
    def __init__(self, x:Decimal, y:Decimal, operation:Callable[[Decimal, Decimal], Decimal]):
        self.x = x
        self.y = y
        self.operation = operation

    # This method will create an instance of the calculation class
    @staticmethod   
    def createCalc(x: Decimal, y: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        return Calculation(x, y, operation)

    # This method will return the result of the operation (sum, diff, product or division)
    def getOutput(self) -> Decimal:
        # Invoke the stored operation with x and y and return the result/output 
        return self.operation(self.x, self.y)
    
