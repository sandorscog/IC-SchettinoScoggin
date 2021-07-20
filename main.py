from keybert_analysis import *
from string_manipulation import *
from vocab import *

historia_usuario = 'como usuario eu desejo fazer o cadastro de livros na loja'
stop_words = ['a','o','as','os','de','da','do','dos','das', 'no', 'nas', 'na', 'nos']

def main():
    i = KeyBert()

    print('*' * 50)

    historia_limpa = remove_stop_words(historia_usuario, stop_words)
    keyterms_list = i.keybertAnalysis(historia_limpa, 3, 3, 5)
    keyterms_list.sort(key=lambda a: a[1], reverse=True)
    print(keyterms_list)

    aux = contains_create(historia_limpa)
    print(aux[0])

    keyterms_string_list = [i[0] for i in keyterms_list]

    if aux[0] != '':
        main_object(contains_term(keyterms_string_list, aux[0]), aux[0])


if __name__ == '__main__':
    main()


'''
C -> Criar, cadastrar, registrar, adicionar, inserir, gerar
            cadastro,  registro,  adiçao     inserçao
R -> Ler, recuperar, verificar, listar, conferir, buscar, pesquisar, obter
U -> Atualizar, alterar, modificar, redefinir, mudar, trocar, corrigir, acrescentar
D -> deletar, excluir, apagar, retirar, eliminar, tirar, limpar, remover
'''
