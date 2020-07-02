import sqlite3 as sql
import sys

def initialize_database():
    try:
        con = sql.connect('members.db')
        cur = con.cursor()
        cur.execute("SELECT SQLITE_VERSION()")
        data = cur.fetchone()
        print(f'SQLite version: {data}')

        # Check if the table exists. If it doesn't, make a table

        cur.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='members'")
        data = cur.fetchone()
        if data[0] == 0:
            cur.execute("CREATE TABLE members (id TEXT PRIMARY KEY)")
            print('Table members doesn\'t exist: creating new table')
        
        con.commit()

        return 0
    except sql.Error as e:
        print(f'Error: {e.args[0]}')
        return 1

def user_in_hivemind(id):
    try:
        con = sql.connect('members.db')
        cur = con.cursor()
        command = "select * from members where id=?"
        cur.execute(command, (id,))
        response = cur.fetchone()
        if response == None:
            return False
        return True
    except sql.Error as e:
        print(f'Error while retrieving: {e.args[0]}')
        return True


def add_user(id):
    try:
        con = sql.connect('members.db')
        cur = con.cursor()
        command = "INSERT INTO members VALUES (?)"
        cur.execute(command, (id,))
        con.commit()
    except sql.Error as e:
        print(f'Error while inserting: {e.args[0]}')

def remove_user(id):
    try:
        con = sql.connect('members.db')
        cur = con.cursor()
        command = "DELETE FROM members WHERE id=?"
        cur.execute(command, (id,))
        con.commit()
        con.close()
    except sql.Error as e:
        print(f'Error while removing: {e.args[0]}')
