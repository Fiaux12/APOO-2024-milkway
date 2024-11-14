import manipularArquivos 

class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.pontos = 0
        self.save_point = 0

    def criarUsuario(self):
        manipularArquivos.adicionar_usuario(self.nome, self.pontos, self.save_point)
    
    def atualizar(self):
        manipularArquivos.atualizar_pontos(self, self.pontos)




    
        