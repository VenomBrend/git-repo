#!/usr/bin/env python
def decorator_maker(*some_arg):
    def decorator(func):
        def wrapper(*arg, **kwargs):
            arg = arg + some_arg
            return func(*arg, **kwargs)
        return wrapper
    return decorator


@decorator_maker('some new argument', 'one')
def my_func(*arg, **kwargs):
    print(arg)
    print(kwargs)


my_func(10, 20, 30, b=10, q=2)
