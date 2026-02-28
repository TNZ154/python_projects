class x:
    def __init__(self):
        print("Hi")
    def __del__(self):
        print("Bye")
obj = x()
del obj