from keybert_analysis import *
from string_manipulation import *
from vocab import *
from historiaUsuario import *

stop_words = ['a','o','as','os','de','da','do','dos','das', 'no', 'nas', 'na', 'nos']

def main():
    i = KeyBert()

    print('*' * 50)

    user_story = read_user_story()

    user_story_analysis(i, user_story)


if __name__ == '__main__':
    main()


'''
C -> Criar, cadastrar, registrar, adicionar, inserir, gerar
            cadastro,  registro,  adiçao     inserçao
R -> Ler, recuperar, verificar, listar, conferir, buscar, pesquisar, obter
U -> Atualizar, alterar, modificar, redefinir, mudar, trocar, corrigir, acrescentar
D -> deletar, excluir, apagar, retirar, eliminar, tirar, limpar, remover
'''
