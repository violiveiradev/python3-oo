

class Conta:

    def __init__(self, numero, titular, saldo, limite = 1000.0) -> None:
        print("Construindo objeto...{}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
