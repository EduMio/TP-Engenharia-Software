import sqlite3
from sqlite3 import Error


def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def select_all_lead(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM lead")

def select_nameclient_lead(conn,cliente):
    cur = conn.cursor()
    cur.execute("SELECT * FROM lead WHERE nome_cliente =? ",(cliente,))
    
def select_user_lead(conn,cliente):
    cur = conn.cursor()
    cur.execute("SELECT * FROM lead WHERE nome_vendedor =? ",(cliente,))

def select_namecompany_lead(conn,cliente):
    cur = conn.cursor()
    cur.execute("SELECT * FROM lead WHERE name_company =?",(cliente,))


