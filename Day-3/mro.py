class A:

    def hello(self):
        print("A")


class B:

    def hello(self):
        print("B")


class C(A, B):
    pass


obj = C()
obj.hello()

print(C.__mro__)