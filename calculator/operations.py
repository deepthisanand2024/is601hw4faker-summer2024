from decimal import Decimal

# Included type hints for input parameter types and return types
def add(x:Decimal, y:Decimal) -> Decimal:
    return x + y

def subtract(x:Decimal, y:Decimal) -> Decimal:
    return x - y

def multiply(x:Decimal, y:Decimal) -> Decimal:
    return x * y
        
def divide(x:Decimal, y:Decimal) -> Decimal:
    if y != 0:
        return x / y
    else:
        raise ValueError("Error: Division by zero")
        
