

class Conta:

    def __init__(self, numero, titular, saldo, limite = 1000.0) -> None:
        print("Construindo objeto...{}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite


    def extrato(self):
        print("Seu saldo é {}".format(self.saldo))

    
    def deposita(self, valor):
        self.saldo += valor

    
    def saca(self, valor):
        self.saldo -= valor
