import MySQLdb
import json
from crud_sql import *

def object_confirmation(object):
    confirmation = False
    response = ''

    print(object)
    response = input('Confirma objeto?')

    if(response[0] == 's' or response[0] == 'S'):
        confirmation = True

    return confirmation


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
        print(similar)
        pass
    else:
        pass
        # atributos completos

    # confirma?


    return #list de tables
