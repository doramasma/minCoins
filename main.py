import sys
import argparse
import logging
import time

from fileParser.fileReader import fileToArray
from Coins.minCoinCalculator import minCoinCalculator

# getParameters - Use of argparse for get the parameters of the command line.
# We define -time for time mode (shows how much time it cost ), -tabulation for 
# tabulation mode (do memoization and tabulation at the same time) and an integer
# for the parameter value.
def getParameters():
    parser = argparse.ArgumentParser()
    parser.add_argument("-time","--time", help="Use -t for enable time mode: calculate the time",
                        action="store_true")
    parser.add_argument("-tabulation","--tabulation", help="Print tabulation implementation result",
                        action="store_true")
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer')                     
    args = parser.parse_args()
    global tabul
    tabul = 0
    global timer
    timer = 0
    if not args.integers:
            logging.exception("Value is required")
            sys.exit(2)
    if args.tabulation:
        tabul = 1
    if args.time:
        timer = 1
    return args.integers[0]
   


if __name__ == '__main__':
    value = getParameters()
    Coins = fileToArray("test.txt")  

    if tabul == 1:
        if timer == 1:
            start = round(time.time() * 1000)
            result = minCoinCalculator(Coins).minCoinsMemoization(value)
            print("MEMOIZATION:     Number of coins needed is: " + str(result) + " TIME: "+ str(round(round(time.time() * 1000) - start)) + "ms")
            
            start = round(time.time() * 1000)
            result = minCoinCalculator(Coins).minCoinsMemoization(value)
            print("TABULATION:      Number of coins needed is: " + str(result) + " TIME: "+ str(round(round(time.time() * 1000) - start)) + "ms")

        else:
            result = minCoinCalculator(Coins).minCoinsMemoization(value)
            print("MEMOIZATION:     Number of coins needed is: " + str(result))
    
            result = minCoinCalculator(Coins).minCoinsTabulation(value)
            print("TABULATION:     Number of coins needed is: " + str(result))

    else:
        if timer == 1:
            start = round(time.time() * 1000)
            result = minCoinCalculator(Coins).minCoinsMemoization(value)
            print("Number of coins needed is: " + str(result) + " TIME: "+ str(round(round(time.time() * 1000) - start)) + "ms")
            
        else:
            result = minCoinCalculator(Coins).minCoinsMemoization(value)
            print("Number of coins needed is: " + str(result))
            