# coding: utf-8
def func(required_arg, *args, **kwargs):
    print(required_arg)
    if args:
        for i, arg in enumerate(args):
            print(i, arg)
    if kwargs:
        for key, item in kwargs.items():
            print(key, item)
            
func("hello")
func("hello", 1,2,3)
func("hello", 1,2,3, goodbye="goodbye")
