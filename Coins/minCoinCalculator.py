import array as arr
import sys

class minCoinCalculator:


    def __init__(self, lista):   
        self.lista = lista
        self.minValuesCache = dict()
        self.minValuesCache[0] = 0


    # Calculates the minimum number of coins of a infinite set of them to get at determinated value by memoization.
    # @return: return the minimum number of coins for the value request.
    def minCoinsMem(self,value):
        if value == 0:
            return 0
        if value in self.minValuesCache:
            return self.minValuesCache[value]
        self.minValuesCache[value] = sys.maxsize
        for coin in self.lista:
            if coin <= value:
                subResult = self.minCoinsMem(value - coin)
                if (subResult != sys.maxsize) and (subResult + 1 < self.minValuesCache[value]):
                    self.minValuesCache[value] = subResult + 1
        return self.minValuesCache[value]

    
    # Control the overFlow due to Dynamic Programming limitations.
    # @return: The minimum number of coins or return -1 when an exception happen
    def minCoinsMemoization(self,value):
        try:
            return self.minCoinsMem(value)
        except OverflowError:
            return -1



    # Calculates the minimum number of coins of a infinite set of them to get 
    # at determinated value by tabulation, the solution is based on Source: geekforgeeks.org
    # @return: return the minimum number of coins for the value request.
    def minCoinsTab(self,value):

        table = [0 for i in range(value + 1)]
        table[0] = 0
        for i in range(1,value + 1):
            table[i] = sys.maxsize 

        for i in range(1,value + 1):
            for coin in self.lista:
                if coin <= i:
                    subResult = table[i - coin]
                    if (subResult != sys.maxsize) and ((subResult + 1) < table[i]):
                        table[i] = subResult + 1
                        
        return table[value]

    
    # Control the overFlow due to Dynamic Programming limitations.
    # @return: The minimum number of coins or return -1 when an exception happen
    def minCoinsTabulation(self,value):
        try:
            return self.minCoinsTab(value)
        except OverflowError:
            return -1    