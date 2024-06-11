''' This class will have the class methods to execute the businss logic for the calculator program '''
from decimal import Decimal
from typing import Callable, List

from calculator.calculation import Calculation

class calculationLogic:

    history: List[Calculation] =[]

    @classmethod
    def addHistory(cls, calculation: Calculation):
        ''' Adds the calculation to the history list '''
        cls.history.append(calculation)

    @classmethod
    def getHistory(cls) -> List[Calculation] :
        ''' Retrieve the calculation history list '''
        return cls.history

    @classmethod
    def clearHistory(cls) -> List[Calculation]:
        ''' Clears the history list '''
        return cls.history.clear()

    @classmethod
    def getLastCalc(cls) -> Calculation:
        ''' Retrieve the most recent calculation from the history list '''
        if len(cls.history)>0:
            return cls.history[-1]
        return None

