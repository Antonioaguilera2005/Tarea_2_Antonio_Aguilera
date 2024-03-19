class Pared:

    def __init__(self, orientacion):

        self.orientacion = orientacion


class ParedCortina(Pared):

    def __init__(self, orientacion, superficie):

        super().__init__(orientacion)

        self.superficie = superficie


class Ventana:

    def __init__(self, pared, superficie, proteccion=None):

        if proteccion is None:

            raise Exception("Protección obligatoria")

        self.pared = pared

        self.superficie = superficie

        self.proteccion = proteccion


class Casa:

    def __init__(self, paredes):

        self.paredes = paredes


    def superficie_acristalada(self):

        superficie_total = 0

        for pared in self.paredes:

            if isinstance(pared, ParedCortina):

                superficie_total += pared.superficie

            else:

                for ventana in self.obtener_ventanas_en_pared(pared):

                    superficie_total += ventana.superficie

        return superficie_total


    def obtener_ventanas_en_pared(self, pared):

        ventanas = []

        for atributo in vars(self).values():

            if isinstance(atributo, Ventana) and atributo.pared == pared:

                ventanas.append(atributo)

        return ventanas



pared_norte = Pared("NORTE")

pared_oeste = Pared("OESTE")

pared_sur = Pared("SUR")

pared_este = Pared("ESTE")



try:

    ventana_norte = Ventana(pared_norte, 0.5)

except Exception as e:

    print(e)


try:

    ventana_norte = Ventana(pared_norte, 0.5, None)

except Exception as e:

    print(e)


ventana_oeste = Ventana(pared_oeste, 1, "Persiana")

ventana_sur = Ventana(pared_sur, 2, "Estor")

ventana_este = Ventana(pared_este, 1, "Persiana")


casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este])

print(casa.superficie_acristalada())

casa.paredes[2] = ParedCortina("SUR", 10)

print(casa.superficie_acristalada())
