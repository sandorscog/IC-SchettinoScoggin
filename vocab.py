'''
C -> Criar, cadastrar, registrar, adicionar, inserir, gerar
            cadastro,  registro,  adiçao     inserçao
R -> Ler, recuperar, verificar, listar, conferir, buscar, pesquisar, obter
U -> Atualizar, alterar, modificar, redefinir, mudar, trocar, corrigir, acrescentar
D -> deletar, excluir, apagar, retirar, eliminar, tirar, limpar, remover
'''

vocab_create = ['criar', 'cadastrar', 'registrar', 'adicionar', 'inserir',
                 'gerar', 'cadastro','registro', 'adição', 'inserção', 'incluir', 'inclusão']

# returns a word from the create vocab if there is one and its position, else it returns an empity
# string and -1 as the position
def contains_create(string):
    for i in vocab_create:
        aux = string.find(i)
        if aux != -1:
            return (i, aux)
    return ('', -1)


def contains_term(string_list, term):
    return [i for i in string_list if term in i]


def main_object(list, term):
    final = ''

    for i in list:
        position = i.find(term)
        position += len(term)
        str = i[position:]
        if str != '':
            str = str.strip()
            str = str.lower()
            final= str

    return final
