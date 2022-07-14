import logging
import sys
from functools import reduce
logging.basicConfig(filename="test29.log",level=logging.DEBUG)
#try to print the prime numbers between 1 to 1000
try:
    class homework:
        def prime_num(self, n):
            for i in range(1, n):
                if i > 1:
                    for m in range(2, i):
                        if i % m == 0:
                            break
                    else:
                        logging.info(i)


    numbers = homework()
    logging.info(numbers.prime_num(1000))
except(ValueError,NameError):
    logging.info("plz enter an integer")

#2.Try to write a function which is replica of list append,extend,pop function?
try:
    class replica:
        def append(self, j, n):
            K = [3, 4, 5, 6]
            K.insert(j, n)
            logging.info(K)

        def extend(self, m, list):
            F = [40, 45, 50, 55]
            F.insert(m, list)
            logging.info(F)

        def pop(self, k):
            g = [34, 6, 7, 89, 9]
            g.remove(k)
            logging.info(g)
    suraj = replica()
    aman= replica()
    jeevan = replica()
    logging.info(suraj.append(2,4))
    logging.info(aman.extend(2,[20,40]))
    logging.info(jeevan.pop(7))

except(NameError,ValueError):
    Logging.info("Beta mani,padhai likhai chhod do,tumse na ho payega")

#3.Try to write a lambda function which can return a concatination of all strings you pass?
try:
    class concatination:
        def addition(self, d):
            result = reduce(lambda x, y: x + y, d)
            logging.info(result)


    ho = concatination()
    logging.info(ho.addition(('456', 'str')))
except(NameError,ValueError):
    Logging.info("Beta mani,padhai likhai chhod do,tumse na ho payega")

#4.try to write a lambda function which can return list of all squares between 1 to 100?
try:
    class square:
        def doguna_lagaan(self, n):
            lst = list(range(1, n + 1))
            logging.info(list(map(lambda x: x * x, lst)))


    hi = square()
    logging.info(hi.doguna_lagaan(100))
except(NameError,ValueError):
    logging.info("Beta mani,padhai likhai chhod do,tumse na ho payega")
#5.try to write a function which can perform read operation from txt file
class padho:
    def padhai(self,s):


        s = open("txt.routine", "r")
        if s.mode == "r":
            contents = s.read()
            logging.info(contents)


turn=padho()
logging.info(turn.padhai(56))

#6.try to write a funcion which is equivalent to print function in python
class human:
    def stary(self,content):
        p=sys.stdout.write(content)
        logging.info(p)
upar=human()
logging.info(upar.stary("naacho"))



















