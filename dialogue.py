import MySQLdb
import json
from crud_sql import *
from sql_gen import *

def object_confirmation(object): # object is a tuple (name, [attributes])

    print('Nome:\n' + object[0] + '\nAtributos: ')
    print(object[1])

    response = input('Confirma esse objeto?(sim/nao): ')
    response = response.lower()

    if(response == 'sim'):
        return True
    else:
        return False


def similar_objects(name, sql_cursor):
    select_query = select('objects', '*', 'name = \'' + name + '\'')

    sql_cursor.execute(select_query)
    results = sql_cursor.fetchall()

    return results


def object_attributes():
    #attribute_tuple_list.append((key, type))
    attribute_tuple_list = []
    attributes_dictionary = {}

    print('Leitura dos atributos para seu objeto: ')
    print('Entre com a palavra "fim" para encerrar a leitura')

    attribute = input()
    attribute = attribute.lower()
    while attribute != 'fim':

        with open('attributes_vocab.json', 'r') as config_file:
            attributes_vocab_json = config_file.read()

        attributes_dictionary = json.loads(attributes_vocab_json)

        if attribute in attributes_dictionary:
            type = attributes_dictionary[attribute]
            attribute_tuple_list.append((attribute, type))
        else:
            type = 'VARCHAR(100)'
            attribute_tuple_list.append((attribute, type))

        attribute = input()
        attribute = attribute.lower()

    return attribute_tuple_list


def define_tables(object, sql_con, sql_cursor):

    tables = []

    # try to find similar objs
    similar = similar_objects(object, sql_cursor)

    if similar != None:
        # verificar semelhança
        # if para ler atributos
        for i in similar:
            sql_attributes = json.loads(i[2])
            attributes_names = []
            attribute_tuple_list = []

            for key, type in sql_attributes.items():
                attributes_names.append(key)
                attribute_tuple_list.append((key, type))

            confirmed = object_confirmation((object, attributes_names))
            if confirmed:
                tables.append(Table(object, attribute_tuple_list)) # define a table
                break

        if not confirmed:
            attributes_tuple_list = object_attributes()
            tables.append(Table(object, attributes_tuple_list))
            # object_attributes

    else:
        # object_attributes
        item_name = input('Qual o nome do item a ser adicionado?')
        attributes_tuple_list = object_attributes()
        tables.append(Table(item_name, attributes_tuple_list))


    # confirma?
    wants_to_add = input('Deseja adicionar outro item ao catalago?(sim/nao)')
    wants_to_add = wants_to_add.lower()

    while wants_to_add == 'sim':
        item_name = input('Qual o nome do item a ser adicionado?')
        attributes_tuple_list = object_attributes()
        tables.append(Table(item_name, attributes_tuple_list))

        wants_to_add = input('Deseja adicionar outro item ao catalago?(sim/nao)')
        wants_to_add = wants_to_add.lower()

    return tables #list de tables
