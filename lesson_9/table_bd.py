import requests
import sqlalchemy
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy import text


class Table_bd:
    __scripts = {
        "select": "select * from company",
        "select only active": "select * from company whwre \"isActive\" = true",
        "select company by id": text("select * from company where id = :id"),
        "delete by id company": text("delete from company where id = :delete"),
        "delete empl": text("delete from employee  where company_id = :id"),        
        "insert new company": text("insert into company(\"name\") values (:new_name)"),
        "insert new empl": text("insert into employee(\"first_name\", \"last_name\", \"phone\", \"company_id\") values (':first_name_new', ':last_name_new', ':phone_new', :id)"),        
        "get max id": "select MAX(id) from company",
        "get empl in company": text("select * from employee e where company_id  = :get_id")
    }

    def __init__(self, connect):
        self.__db = create_engine(connect)

    def create(self, name):
        self.__db.execute(self.__scripts["insert new company"], new_name = name)

    def get_company(self, id):
        return self.__db.execute(self.__scripts["select company by id"], id = id).fetchall()

    def get_max_id_company(self):
        return self.__db.execute(self.__scripts["get max id"]).fetchall()[0][0]

    def delete_company(self, id_company):
        self.__db.execute(self.__scripts["delete by id company"], delete = id_company)

    def add_new_empl(self, f_name, l_name, p_new, id_company):
        self.__db.execute(
            self.__scripts["insert new empl"], first_name_new = f_name, last_name_new = l_name, phone_new = p_new, id = id_company)

    def get_empl_in_company(self, max_id):
        return self.__db.execute(self.__scripts["get empl in company"], get_id = max_id).fetchall()

    def delete_empl(self, id_empl):
        self.__db.execute(self.__scripts["delete empl"], id = id_empl)

