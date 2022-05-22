import sqlite3
from sqlite3 import Error


def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def select_all_tasks(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")

def select_nameclient_task(conn,cliente):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE nome_cliente =? ",(cliente,))
    
def select_user_task(conn,cliente):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE nome_vendedor =? ",(cliente,))

def select_namecompany_task(conn,cliente):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE name_company =?",(cliente,))
