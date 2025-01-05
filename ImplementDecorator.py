def decorator(func):
    def wrapper():
        print("Execution Initiated")
        func()
        print("Execution Completed")
        
    return wrapper
    

@decorator
def hello():
    print("Execution...")

hello()