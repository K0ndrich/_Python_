def my_decorator(my_func):

    def wrapper(*args, **kwargs):
        print("BEFORE")
        result = my_func(*args, **kwargs)
        print("AFTER")
        return result

    return wrapper


@my_decorator
def say_hi():
    print("hello")
    return 1


say_hi()
