class Programa:
    def __init__(self, nome, ano) -> None:
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    
    @property
    def likes(self):
        return self._likes
    

    def dar_likes(self):
        self._likes += 1

    
    @property
    def nome(self):
        return self._nome
    

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def __str__(self) -> str:
        return f"Nome: {self._nome} - Likes: {self._likes}"


class Filme(Programa):
    def __init__(self, nome, ano, duracao) -> None:
        super().__init__(nome, ano)
        self.duracao = duracao


    def __str__(self) -> str:
        return f"Nome: {self._nome} - Duração: {self.duracao} - Ano: {self.ano} - Likes: {self._likes}"

    
class Serie(Programa):
    def __init__(self, nome, ano, temporada) -> None:
        super().__init__(nome, ano)
        self.temporade = temporada
    

    def __str__(self) -> str:
        return f"Nome: {self._nome} - Temporadas: {self.temporade} - Ano: {self.ano} - Likes: {self._likes}"

class Playlist():
    def __init__(self, nome, programas) -> None:
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('todo mundo em panico', 1999, 100)
demolidor = Serie('demolidor', 2016, 2)


vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()

lista_programas = [atlanta, vingadores, demolidor, tmep]
minha_playlist = Playlist('fim de semana', lista_programas)

for programa in minha_playlist:
    print(programa)
