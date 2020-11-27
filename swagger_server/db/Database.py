import os
import psycopg2

from swagger_server.db.queries import *

DATABASE_HOST = os.getenv("DATABASE_HOST", "ec2-54-247-71-245.eu-west-1.compute.amazonaws.com")
DATABASE_NAME = os.getenv("DATABASE_NAME", "de57281eskpa")
DATABASE_USER = os.getenv("DATABASE_USER", "xnclbvmyvttwgi")
DATABASE_PASS = os.getenv("DATABASE_PASS", "75c8efa2c751e7ee71f3aa2b8f39a45c1a4896d4d06879ecaba08ac47ffd667b")


class PostgresDB:

    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = psycopg2.connect(host=DATABASE_HOST, dbname=DATABASE_NAME, user=DATABASE_USER,
                                     password=DATABASE_PASS,
                                     port=5432)

    def __execute(self, query, args=None):
        __cursor = self.conn.cursor()
        __cursor.execute(query, args)
        __output = []

        if __cursor.description is not None:
            for item in __cursor:
                __output.append(item)
        __cursor.close()
        return __output

    def close(self):
        self.conn.commit()
        self.conn.close()

    def get_account_by_id(self, account_id: int):
        self.connect()
        locations = self.__execute(GET_ACCOUNT_BY_ID, {"account_id": account_id})
        self.close()
        return locations

    def delete_account(self, account_id: int):
        self.connect()
        last_location = self.__execute(DELETE_ACCOUNT, {"account_id": account_id})
        self.close()
        return last_location

    def add_new_account(self, username: str, password: str, birthdate: str, age: int):
        self.connect()
        self.__execute(NEW_ACCOUNT, {"username": username, "password": password, "birthdate": birthdate, "age": age})
        self.close()

    def update_account(self, account_id: int, password: str = ''):
        self.connect()
        self.__execute(UPDATE_ACCOUNT, {"account_id": account_id, "password": password})
        self.close()

    def get_account_id_by_username(self, username: str):
        self.connect()
        account_id = self.__execute(GET_ACCOUNT_ID_BY_USERNAME, {"username": username})
        self.close()
        return account_id

    def get_account_id_by_username_and_password(self, username: str, password: str):
        self.connect()
        account_id = self.__execute(
            GET_ACCOUNT_ID_BY_USERNAME_AND_PASSWORD, {"username": username, "password": password})
        self.close()
        return account_id
