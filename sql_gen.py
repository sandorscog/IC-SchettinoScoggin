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

    def __init__(self, schema, table_name, attributes=None):
        self.schema = schema
        self.table_name = table_name
        self.columns = attributes
        self.file = open(schema + '.sql', 'w')
        self.file.close()


    def create_header(self):
        return "SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;\nSET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;\nSET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';"


    def create_schema(self):
        sql = 'CREATE SCHEMA IF NOT EXISTS `' + self.schema + '` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;\n'
        sql += 'USE `' + self.schema + '`;'
        return sql


    def create_table(self):
        sql = 'CREATE TABLE IF NOT EXISTS `' + self.schema + '`.`' + self.table_name + '`('
        sql += '`id'+ self.table_name + '` INT NOT NULL AUTO_INCREMENT, `name` VARCHAR(45) NOT NULL, PRIMARY KEY (`id'+ self.table_name +'`)) ENGINE = InnoDB;'
        return sql


    def create_ending(self):
        return "SET SQL_MODE=@OLD_SQL_MODE;SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;"


    def write_in_file(self, text):
        self.file = open(self.schema + '.sql', 'w')
        self.file.write(text)
        self.file.close()


    def generate_script(self):
        script = self.create_header()
        script += self.create_schema()
        script += self.create_table()
        script += self.create_ending()
        return script


sql = SQL('pessoas', 'pessoa')
sql.write_in_file(sql.generate_script())
