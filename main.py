from keybert_analysis import *
from string_manipulation import *

historia_usuario = 'eu como usuario gostaria de cadastrar os estados do meu pais'
stop_words = ['a','o','as','os','de','da','do','dos','das']

def main():
    i = KeyBert()

    print('*' * 50)

    historia_limpa = remove_stop_words(historia_usuario, stop_words)
    keyword_list = i.keybertAnalysis(historia_limpa, 3, 3, 5)
    keyword_list.sort(key=lambda a: a[1], reverse=True)
    print(keyword_list)




if __name__ == '__main__':
    main()


'''
C -> Criar, cadastrar, registrar, adicionar, inserir, gerar
            cadastro,  registro,  adiçao     inserçao
R -> Ler, recuperar, verificar, listar, conferir, buscar, pesquisar, obter
U -> Atualizar, alterar, modificar, redefinir, mudar, trocar, corrigir, acrescentar
D -> deletar, excluir, apagar, retirar, eliminar, tirar, limpar, remover
'''
