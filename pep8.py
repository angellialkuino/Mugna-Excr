import math, datetime

def takeAllList(arg1,
    arg2, arg3 = 0, *args, 
    **kwargs):
    """
    Docstring for take_all_list. Basically, this is a useless function, but would test how well you know about PEP-8.
    """
    list_a = [1,2,
    3,4,
    5]
    var_b = list_a[0] * list_a[1] + list_a[2] - (3 + list_a[3])
    print(arg1, arg2)
    if not arg3 is 0:
        print(arg3)
    if ( arg3>5 and arg3<10 ):
        list_a.append(
            arg3
        )
        print("This is to ensure that our list would be printed ==> {}".format(list_a))
    else:
        list_a = None
    print(var_b)
    if list_a != None:
        print("list_a has an entry")

def printAllNumber(n):
    m      =0
    first  =n
    second =n+1
    third  =n+2
    fourth =n+3
    print(first , second , third , fourth)
    for n in (range( n )):
        print(n)    #This will print n
        m+=n       #This will increment m with n
        print(m)    #This will print m
    checker = m>sum(range(n))
    if checker == True:
        print("TAMA!") 
    else:
        print("MALI!")

from math import sqrt
from os import *

class this_is_student_class():
    FIRSTNAME = 'A'
    LASTNAME = 'A'
    def __init__(this, age, address):
        this.AGE = age
        this.ADDRESS = address
    def getName(this):
        return "%s, %s" % (this.LASTNAME, this.FIRSTNAME)
def AnotherFunction():
    # This will do something. I promise.
    print(math.pi)
    sqrt_of_pi = sqrt(math.pi)
    print('It\'s the square root of pi' , sqrt_of_pi)
    string_sample = "Why, hello there!"
    print(string_sample[ 1 : : 2])
    takeAllList (1,2,3)
    try: l = 2; m = 3; n = l+m;
    except:
        print("ERROR!")
        return math.pi
    takeAllList (l,m,n)
