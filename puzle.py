class Base:

    def __init__(self):

        self.a = "a"

        self.b = "b"

        self.c = "c"


    def A(self):

        print(self.a)


    def B(self):

        print(self.b)


    def C(self):

        print(self.c)


class Derivada(Base):

    def __init__(self):

        self.a = "aa"

        super().__init__()

        self.c = "cc"


    def A(self):

        print(self.a)


    def B(self):

        self.b = "bb"

        super().B()

        print(self.b)


base = Base()

derivada = Derivada()


base.A()

derivada.A()


print()


base.B()

derivada.B()

base.C()

derivada.C()

derivada = base

derivada.C()  