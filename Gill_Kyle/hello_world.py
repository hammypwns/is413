"""
Testing random stuff fam.
"""


MSG = "Hello World"
MYINT = 5
MYFLOAT = 6.2
ONESTRING = "My"
TWOSTRING = "First"
THREESTRING = "Sentence"
MYSPACE = " "
MYPERIOD = "."


print(MYINT)
print(MYFLOAT)
MYADD = MYINT + MYFLOAT

print(MYINT + MYFLOAT)
print(MYADD)
print(MSG)
print(ONESTRING + " " + TWOSTRING + MYSPACE + THREESTRING + MYPERIOD)

NUMTIMES = 3


"""
Testing parameter passing and .
"""

def my_func(param1, param2):
    print("this is my func")
    print("Observe that the string %s will be displayed %d times. Again, %i times"
          %(param1, param2, param2))
    for i in range(param2):
        print(param1)

my_func(MSG, NUMTIMES)
