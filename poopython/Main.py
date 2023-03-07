class Main:
    pass 

from Cliente import Cliente
from Conta import Conta

c1 =  Cliente ("João","88992450206")
conta = Conta (c1.nome,6563,0)
print(conta.titular, "Numero" , conta.numero,"Seu saldo",conta.saldo)