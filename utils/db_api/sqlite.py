from datetime import date
import sqlite3
from time import time


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(
            self,
            sql: str,
            parameters: tuple = None,
            fetchone=False,
            fetchall=False,
            commit=False,
    ):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
            CREATE TABLE Users (
                id int NOT NULL,
                Name varchar(255) NOT NULL,
                email varchar(255),
                phone varchar(255),
                language varchar(3),
                is_operator BOOLEAN DEFAULT FALSE,
                
                PRIMARY KEY (id)
            );
        """
        self.execute(sql, commit=True)

    def create_table_appeal(self):
        sql = """
            CREATE TABLE Appeal (
                id int NOT NULL,
                user_id int NOT NULL,
                text varchar(255),
                theme varchar(255),
                type varchar(255),
                status varchar(255),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                
                PRIMARY KEY (id),
                FOREIGN KEY (user_id) REFERENCES Users(id)
            );
        """
        self.execute(sql, commit=True)

    def create_table_replies(self):
        sql = """
            create table Replies (
                id int NOT NULL,
                appeal_id int NOT NULL,
                user_id int NOT NULL,
                reply_id int NULL,
                text varchar(255),
                message_id int NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                
                PRIMARY KEY (id),
                FOREIGN KEY (appeal_id) REFERENCES Appeal(id)
                FOREIGN KEY (user_id) REFERENCES Users(id)
                FOREIGN KEY (reply_id) REFERENCES Replies(id)
            );
        """
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([f"{item} = ?" for item in parameters])
        return sql, tuple(parameters.values())

    def add_user(self, id: int, name: str, email: str = None, language: str = "uz"):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Users(id, Name, email, language) VALUES(?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id, name, email, language), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def update_user_email(self, email, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = """
        UPDATE Users SET email=? WHERE id=?
        """
        return self.execute(sql, parameters=(email, id), commit=True)

    def update_user_phone(self, phone, id):
        sql = """
        UPDATE Users SET phone=? WHERE id=?
        """
        return self.execute(sql, parameters=(phone, id), commit=True)

    def update_user_language(self, language, id):
        sql = """
        UPDATE Users SET language=? WHERE id=?
        """
        return self.execute(sql, parameters=(language, id), commit=True)

    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)

    def get_appeals(self):
        sql = """
        SELECT * FROM Appeal
        """
        return self.execute(sql, fetchall=True)

    def create_appeal(self, user_id, text, type, status, theme=None) -> int:
        sql = """
        INSERT INTO Appeal(id, user_id, text, type, status, theme) VALUES(?, ?, ?, ?, ?, ?)
        """
        id = int(time())
        self.execute(
            sql, parameters=(id, user_id, text, type, status, theme), commit=True
        )
        return id

    def get_appeal(self, id):
        sql = """
        SELECT * FROM Appeal WHERE id=?
        """
        return self.execute(sql, parameters=(id,), fetchone=True)

    def get_appeals_by_user_id(self, user_id):
        sql = """
        SELECT * FROM Appeal WHERE user_id=?
        """
        return self.execute(sql, parameters=(user_id,), fetchall=True)

    def get_appeals_by_type(self, type):
        sql = """
        SELECT * FROM Appeal WHERE type=?
        """
        return self.execute(sql, parameters=(type,), fetchall=True)

    def update_appeal_status(self, status, id):
        sql = """
        UPDATE Appeal SET status=? WHERE id=?
        """
        return self.execute(sql, parameters=(status, id), commit=True)

    def create_reply(self, appeal_id, user_id, text, reply_id=None, message_id=None):
        sql = """
        INSERT INTO Replies(id, appeal_id, user_id, text, reply_id, message_id) VALUES(?, ?, ?, ?, ?, ?)
        """
        id = int(time())
        self.execute(
            sql, parameters=(id, appeal_id, user_id, text, reply_id, message_id), commit=True
        )
        return id

    def get_replies(self, **kwargs):
        sql = "SELECT * FROM Replies WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        sql += " ORDER BY created_at DESC"
        return self.execute(sql, fetchall=True)

    def get_reply(self, **kwargs):
        sql = "SELECT * FROM Replies WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        sql += " ORDER BY created_at DESC"
        return self.execute(sql, parameters=parameters, fetchone=True)

    def get_replies_by_user_id(self, user_id):
        sql = """
        SELECT * FROM Replies WHERE user_id=?
        """
        return self.execute(sql, parameters=(user_id,), fetchall=True)

    def get_replies_by_appeal_id_and_user_id(self, appeal_id, user_id):
        sql = """
        SELECT * FROM Replies WHERE appeal_id=? AND user_id=? ORDER BY created_at DESC
        """
        return self.execute(sql, parameters=(appeal_id, user_id), fetchall=True)


def logger(statement):
    print(
        f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
"""
    )
