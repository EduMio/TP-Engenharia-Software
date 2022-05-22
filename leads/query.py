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
    cur.execute("SELECT * FROM leads_lead")

def select_nameclient_lead(conn,cliente):
    cur = conn.cursor()
    cur.execute("SELECT * FROM leads_lead WHERE first_name =? ",(cliente,))
    
def select_user_lead(conn,cliente):
    cur = conn.cursor()
    cur.execute("SELECT * FROM leads_lead WHERE nome_vendedor =? ",(cliente,))

def select_namecompany_lead(conn,cliente):
    cur = conn.cursor()
    cur.execute("SELECT * FROM leads_lead WHERE name_company =?",(cliente,))


