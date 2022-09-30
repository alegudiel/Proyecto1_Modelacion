from cmath import inf
import random
import math
# multiples servidores

# Time of arrival of the next request
def funcExp(lamVal):
    return  - float((1/lamVal)*math.log(random.random()))

