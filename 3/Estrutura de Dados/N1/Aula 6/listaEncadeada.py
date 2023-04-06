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

    def insereNoInicio(self, n):
        n.setProximo(self.getCabeca().getProximo())
        self.getCabeca().setProximo(n)

    def retiraNoInicio(self):
        ret = None
        if not self.listaVazia():
            ret = self.getCabeca().getProximo()
            self.getCabeca().setProximo(ret.getProximo())
            ret.setProximo(None)
        return ret
    
    def retiraNoFim(self):
        ret = None
        if not self.listaVazia():
            ant = self.getCabeca()
            atual = self.getCabeca().getProximo()
            while atual.getProximo() != None:
                ant = atual
                atual = atual.getProximo()
            ret = atual
            ant.setProximo(None)
        return ret

    def insereNoFim(self, n):
        ant = self.getCabeca()
        atual = self.getCabeca().getProximo()
        while atual != None:
            ant = atual
            atual = atual.getProximo()
        ant.setProximo(n)                

    def mostraLista(self):
        atual = self.getCabeca().getProximo()
        while atual != None:
            print(atual.getDados().getValores())
            atual = atual.getProximo()