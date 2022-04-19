from documento import Documento
from TelefonesBr import TelefonesBr
import re

cpf1 = Documento.cria_novo("37661797801")

print(cpf1)

cnpj1 = Documento.cria_novo("00416968000101")

print(cnpj1)




telefone = "552126481234"

telefone_objeto = TelefonesBr(telefone)

#padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
#resposta = re.search(padrao,telefone)
#print(resposta.group())

telefone_objeto.format_numero()