# def sacar(self, valor:float) -> None:
#     if self.saldo   >= valor:
#         self.saldo-=valor
#    
#
def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado!")
        print("retire seu dinehiro na boca do caixa")
    
    print("obrigado por ser nosso cliente")

def depositar(valor):
    saldo = 500
    saldo+= valor

depositar(200)
sacar(200)

##sacar(saldo)





