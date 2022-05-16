class No:
    def __init__(self, dado):
        self.dado = dado
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None
    
    def inserir(self, dado):
        self.raiz = self.inserir_aux(dado, self.raiz)


    def inserir_aux(self, dado, no):
        if no == None:
            return No(dado)
        elif dado < no.dado:
            no.esquerda = self.inserir_aux(dado, no.esquerda)
        else:
            no.direita = self.inserir_aux(dado, no.direita)
        
        return no




    def printERD(self):
        self.printERD_aux(self.raiz)


    def printERD_aux(self, no):
        if no != None:
            self.printERD_aux(no.esquerda)
            print(no.dado)
            self.printERD_aux(no.direita)
    

arvore = ArvoreBinariaBusca()
arvore.inserir(7)
arvore.inserir(3)
arvore.inserir(2)
arvore.inserir(5)
arvore.inserir(6)
arvore.printERD()