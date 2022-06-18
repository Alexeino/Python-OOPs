class A:
    def f(self):
        print("A")

class B(A):
    def f(self):
        print("B")
class C(B):
    def f(self):
        print("C")

c = C()
b = B()
c.f()
b.f()