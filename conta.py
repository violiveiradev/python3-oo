

class Conta:

    def __init__(self, numero, titular, saldo, limite = 1000.0) -> None:
        print("Construindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


    def extrato(self):
        print("Olá {} seu saldo é {}".format(self.__titular, self.__saldo))

    
    def deposita(self, valor):
        self.__saldo += valor


    def __pode_sacar(self, valor):
        return valor <= self.__saldo + self.__limite
        

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("Saldo insdisponivel para saque.")

    
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    
    def info(self):
        print('Numero: {} \nTitular: {} \nSaldo: {} \nLimite: {}'.format(self.__numero, self.__titular, self.__saldo, self.__limite))


    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite


    @staticmethod
    def codigos_bancos():
        return {"BB":"001", "Caixa":"104", "Bradesco":"237"}
