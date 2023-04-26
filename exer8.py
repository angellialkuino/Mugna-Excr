import time


def timing_decorator(func):
    def inner(*args,**kwargs):
        print("Time it took to run the function:")
        st = time.time()
        func(*args,**kwargs)
        et = time.time()
        diff = (et-st)*1000
        print(f"{diff:.2f} ms")
        return func(*args,**kwargs)
    
    return inner


@timing_decorator
def adding_function(x,y):
    print(f"The sum is {x+y}.")

adding_function(3,5)
