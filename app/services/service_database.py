from decouple import config
from fastapi.responses import JSONResponse
import sqlite3

class DatabaseService:
    def __init__(self):
        self.conn = sqlite3.connect('sqlite.db')
        self.cursor = self.conn.cursor()

    def create_table(self):
        query = '''CREATE TABLE IF NOT EXISTS employees (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    age INTEGER,
                    salary REAL
                );'''
        self.cursor.execute(query)
        self.conn.commit()

    def insert_employee(self, name, age, salary):
        query = '''INSERT INTO employees (name, age, salary)
                    VALUES (?, ?, ?);'''
        self.cursor.execute(query, (name, age, salary))
        self.conn.commit()

    def get_employees(self):
        query = '''SELECT * FROM employees;'''
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows

    def update_employee(self, employee_id, name, age, salary):
        query = '''UPDATE employees
                    SET name = ?, age = ?, salary = ?
                    WHERE id = ?;'''
        self.cursor.execute(query, (name, age, salary, employee_id))
        self.conn.commit()

    def delete_employee(self, employee_id):
        query = '''DELETE FROM employees
                    WHERE id = ?;'''
        self.cursor.execute(query, (employee_id,))
        self.conn.commit()

    def __del__(self):
        self.cursor.close()
        self.conn.close()