import mysql.connector
import psycopg2


class PostgresClient():
    def __init__(self):
        self.db = "postgres"
    
    def get_client():
        return connection = psycopg2.connect(
                user="user",
                password="password",
                host="localhost",
                port="5432"
            )

class MysqlClient():
    def __init__(self):
        self.db = "mysql"

    def get_client():
        return mysql.connector.connect(
                user="user",
                password="password",
                host="localhost",
                port="3306"
            )


def get_client(database="Postgresql"):
    clients = {
        "Postgresql": PostgresClient,
        "Mysql": MysqlClient,
    }
    return clients[database]()


if __name__ = "__main__":
    postgres = get_client(database="Postgresql")
    mysql = get_client(database="Mysql")

    print(f"DB: {postgres.db}, client: {postgres.get_client()}")
    print(f"DB: {mysql.db}, client: {mysql.get_client()}")



