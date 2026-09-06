import time 

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function is called.")
        result = func(*args, **kwargs)
        print("After the function is called.")
        return result
    return wrapper

    def chips(func):
        def wrapper(*args, **kwargs):
            print("Before the function is called.")
            result = func(*args, **kwargs)
            print("After the function is called.")
            return result
        return wrapper
         
@decorator
def get_increase():
    print("Icecream")

get_increase()


def timing_decorator(func): 
    def wrapper():
        start_time = time.time() 
        result = func() 
        end_time = time.time() 
        print(f"Elapsed time: {end_time - start_time}") 
    return wrapper

def wrapper(*args, **kwargs):
        print("Before the function is called.")
        result = func(*args, **kwargs)
        print("After the function is called.")
        return result



def decorator_function(original_function): # 1. Define the decorator function
    def wrapper(): # 2. Define the wrapper function
        print("Starting...")
    original_function() # 3. Call the original function, calls whatever function was passed into decorator_function.
    print("Finished...")
    return wrapper # 4. Return the wrapper

@decorator_function # decorator syntax equivalent to hello = decorator_function(hello)
def hello():
    print("Hello!")
hello()

def decorator_function(original_function): # 1. Define the decorator function
    def wrapper(a,b): # 2. Define the wrapper function
        print("Starting...")
        
        result = original_function(a,b) # 3. Call the original function
        print(result)
        print("Finished...")
        return result ** 2
    return wrapper # 4. Return the wrapper

@decorator_function # final
def hello(a,b):
    return (a+b)
hello(2,2)