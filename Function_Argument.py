def varibleLengthArgExample(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print (arg)
    for key, value in kwargs.items():
        print(key, value)
def main():
# Positional Arguments
# codexplore(3, 2, 1)
# Keyword arguments
# codexplore (a="Hello World", c="C_value", b=2)
# *args:
#varibleLengthArgExample('a','b', "Hello World", 1, 2, 3)
# **kwargs:
    varibleLengthArgExample('a',2, "Hello World", 1, size="Up Size", age="NG")
if __name__=="__main__":
    main()