from traceback import print_tb
from acesso_cep import BuscaEndereco

cep = 14403326
objeto_cep = BuscaEndereco(cep)


# 01001000

print(objeto_cep.via_cep())