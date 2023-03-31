from No import *
from Elemento import *
from listaEncadeada import *

e = Elemento()
e.setChave(1)
e.setNome("Carlos")
n = No(e)

print(e.getChave(), e.getNome())
print(n.getDados().getNome(), n.getProximo())