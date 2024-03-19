class A:

    def __init__(self, a):

        self.a = a


class B(A):

    def __init__(self, a, b):

        super().__init__(a, b)

        self.b = b


class C(A):

    def __init__(self, a, c):

        super().__init__(a,)

        self.c = c


class D(B, C):

    def __init__(self, a, b, c):

        super().__init__(a, b)

        C.__init__(self, a, c)


# Pruebas

d = D(1, 2, 3)

print(isinstance(d, A), isinstance(d, B), isinstance(d, C))

print(d.a, d.b, d.c)
