from No import No

class ListaEncadeada:
    def __init__(self):
        self.__cabeca = No()

    def listaVazia(self):
        return self.__cabeca.getProximo() == None
    
    def getCabeca(self):
        return self.__cabeca
    
    def setCabeca(self, valor):
        self.__cabeca = valor