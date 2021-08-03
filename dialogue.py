import MySQLdb
import json
from crud_sql import *

def object_confirmation(object): # object is a tuple (name, [attributes])

    print('Nome:\n' + object[0] + '\nAtributos: ')
    print(object[1])

    response = input('Confirma esse objeto?(sim/nao): ')
    response.lower()

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
    return


def define_tables(object, sql_con, sql_cursor):

    tables = []

    # try to find similar objs
    similar = similar_objects(object, sql_cursor)


    if similar != None:
        # verificar semelhança
        # if para ler atributos
        for i in similar:
            objects = json.loads(i[2])
            attributes = []
            for key, type in objects.items():
                attributes.append(key)
            if object_confirmation((object, attributes)):
                break
        pass
    else:
        pass
        # atributos completos

    # confirma?


    return #list de tables
