from os import lseek
from termios import CKILL


class Filme:
    def __init__(self, nome, ano, duracao) -> None:
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes
    

    def dar_likes(self):
        self.__likes += 1

    
    @property
    def nome(self):
        return self.__nome
    

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
class Serie:
    def __init__(self, nome, ano, temporada) -> None:
        self.__nome = nome.title()
        self.ano = ano
        self.temporade = temporada
        self.__likes = 0

    
    @property
    def likes(self):
        return self.__likes
    

    def dar_likes(self):
        self.__likes += 1

    
    @property
    def nome(self):
        return self.__nome
    

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    

vingadores = Filme("vingadores - guerra inifita", 2018, 106)
print(vingadores)

atlanta = Serie("atlanta", 2018, 2)
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano}')