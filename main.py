from keybert_analysis import *
from string_manipulation import *
from vocab import *
from historiaUsuario import *
from dialogue import *
import json
import MySQLdb

stop_words = ['a','o','as','os','de','da','do','dos','das', 'no', 'nas', 'na', 'nos']

def main():

    # connection to the sql server
    with open('config.json', 'r') as config_file:
        config_json = config_file.read()

    connect_config = json.loads(config_json)

    sql_con = MySQLdb.connect(host=connect_config['host'], user=connect_config['user'], password=connect_config['password'], db=connect_config['db'])
    sql_cursor = sql_con.cursor()
    # cursor and connection stablished

    i = KeyBert()

    print('*' * 50)

    user_story = read_user_story()

    tables = define_tables(user_story_analysis(i, user_story, stop_words)[0], sql_con, sql_cursor)

    data_base = SQL('zzzzz', tables)
    data_base.write_in_file(data_base.generate_script())

if __name__ == '__main__':
    main()


'''
C -> Criar, cadastrar, registrar, adicionar, inserir, gerar
            cadastro,  registro,  adiçao     inserçao
R -> Ler, recuperar, verificar, listar, conferir, buscar, pesquisar, obter
U -> Atualizar, alterar, modificar, redefinir, mudar, trocar, corrigir, acrescentar
D -> deletar, excluir, apagar, retirar, eliminar, tirar, limpar, remover
'''
