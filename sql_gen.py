"""
CREATE TABLE IF NOT EXISTS `bands`.`record_label` (
  `idrecord_label` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `founding` DATE NULL,
  `location` VARCHAR(45) NULL,
  PRIMARY KEY (`idrecord_label`))
ENGINE = InnoDB;
"""

class SQL:

    def __init__(self, schema, tables): # the constructor must receive the name of the schema and a list
        self.schema = schema            # the list has the specifications of each table from the model
        self.tables = tables            # it is a list o tuples, each tuple has a string and a list of tuples
        self.file = open(schema + '.sql', 'w') # those are composed of 2 strings
        self.file.close()


    def create_header(self):
        return "SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;\nSET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;\nSET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';\n"


    def create_schema(self):
        sql = 'CREATE SCHEMA IF NOT EXISTS `' + self.schema + '` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;\n'
        sql += 'USE `' + self.schema + '` ;\n\n\n\n'
        return sql


    def create_table(self, table): # returns an entity's SQL table
        sql = 'CREATE TABLE IF NOT EXISTS `' + self.schema + '`.`' + table.name + '`(\n'
        sql += '\t`id'+ table.name + '` INT NOT NULL AUTO_INCREMENT,\n'

        for i in table.attributes:
            sql += '\t`' + i[0] + '` ' + i[1] + ' NULL,\n'

        sql += '\tPRIMARY KEY (`id'+ table.name +'`)) \nENGINE = InnoDB;\n\n\n\n'
        return sql


    def create_ending(self): # will return the last information needed in the script
        return "SET SQL_MODE=@OLD_SQL_MODE;\nSET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;\nSET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;\n"


    def write_in_file(self, text):
        self.file = open(self.schema + '.sql', 'w')
        self.file.write(text)
        self.file.close()


    def generate_script(self):    # generates all the sections of the MySQL Script
        script = self.create_header()
        script += self.create_schema()

        for i in self.tables: # iterates over the list of tables and adds the new table to the script
            script += self.create_table(i)

        script += self.create_ending()
        return script

class Table:
    # it is a tuple, it has a string and a list of tuples those are composed of 2 strings
    def __init__(self, name, attributes):
        self.name = name
        self.attributes = attributes
        self.tuple = (name, attributes)

# testing
"""
lista_atributos = [('name', 'VARCHAR(45)'), ('founding', 'DATE')]
tabela = ('band', lista_atributos)

lista_atributos2 = [('name', 'VARCHAR(45)'), ('birthday', 'DATE')]
tabela2 = ('member', lista_atributos2)

lista_atributos3 = [('name', 'VARCHAR(45)'), ('number_of_tracks', 'INT'), ('release', 'DATE')]
tabela3 = ('album', lista_atributos3)

tabelas = [tabela, tabela2, tabela3]
sql = SQL('bands', tabelas)
sql.write_in_file(sql.generate_script())
"""
