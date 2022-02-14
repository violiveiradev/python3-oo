
from conta import Conta

conta = Conta(123, "Nico", 55.5, 1000.0)

conta2 = Conta(547, "Vinicius", 555.5)

conta.extrato()

conta2.extrato()

conta2.transfere(100.0, conta)

conta.extrato()

conta2.extrato()

conta.saca(1000.0)
conta.extrato()


conta.saldo

conta.titular

conta.limite

conta.limite = 9900.0
 
bancos = Conta.codigos_bancos()

print(bancos)