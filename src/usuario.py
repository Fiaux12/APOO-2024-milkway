import manipularArquivos 

class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.pontos = 0
        self.save_point = 0

    def criarUsuario(self):
        # Adiciona usuários usando as funções do arquivo de manipulação
        manipularArquivos.adicionar_usuario(self.nome, self.pontos, self.save_point)
        df_usuarios = manipularArquivos.carregar_usuarios()



    
        