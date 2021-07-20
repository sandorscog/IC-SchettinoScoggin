

def insert(table, values):
    return 'INSERT INTO `' + table + '` VALUES(default, ' + ', '.join(['\'' + i + '\'' if type(i) is str else str(i) for i in values]) + ');'


def update(table, sets, where=None):
    query = 'UPDATE `' + table + '` SET ' + ', '.join([i[0] + " = '" + i[1] + "'" for i in sets])
    if where:
        query += ' WHERE ' + where
    return query


def delete(table, where=None):
    query = 'DELETE FROM ' + table
    if where:
        query += ' WHERE ' + where
    return query


def select(table, fields, where=None):
    query = 'SELECT ' + fields + ' FROM ' + table
    if where:
        query += ' WHERE ' + where
    return query
