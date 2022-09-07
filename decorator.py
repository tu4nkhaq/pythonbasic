# import time
# #Decorators
# def cal_time(func):
#     def cal_seq(*args):
#         start=time.time()
#         result=func(*args)
#         end=time.time()
#         print(func.__name__+" took "+str((end-start)*1000)+"ms")
#         return result
#     return cal_seq
# @cal_time
# def square(numbers):
#     for number in numbers:
#         yield number*number
# @cal_time
# def cube(numbers):
#     for number in numbers:
#         s= number*number*number
#         yield s
# array=range(1,100000)
# out_square=list(square(array))
# out_cube=list(cube(array))
def display_decorator(func):
    def wrapper(str):
        # logic trước khi chạy hàm func
        print(f'Log: The function {func.__name__} is executing ...')
        func(str)
        # logic sau khi chạy hàm func
        print('Log: Execution completed.\n')
    return wrapper

def display(str):
    print(str)

display = display_decorator(display)
display('Hello world')

@display_decorator
def say_hello(str):
    print(str)

say_hello('Hello, Donald')