import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def select_account(conn):
    sql = 'SELECT * FROM account'
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)


def create_account(conn, task):
    sql = ''' INSERT INTO account (Login, Password)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)


def update_account(conn, data):
    sql = ''' UPDATE account
              SET Password = ?
              WHERE Login = ?'''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()


def remove_account(conn, removed_task):
    sql = ''' DELETE FROM account WHERE Login = ?'''
    cur = conn.cursor()
    cur.execute(sql, removed_task)
    conn.commit()


def main():

    database = r"dima.db" 
 
    conn = create_connection(database)

    with conn:
        print("\nВсі нотатки (текст, дата)")
        select_account(conn)
        print("\nВставка нового рядка...")
        create_account(conn, ('Phoenix', '123321'))
        print("\nВсі нотатки (текст, дата)")
        select_account(conn)
        print("\nЗміна рядка...")
        update_account(conn, ('123123321321', 'Phoenix'))
        print("\nВсі нотатки (текст, дата)")
        select_account(conn)
        print("\nВидалення рядка")
        remove_account(conn, ('Phoenix',))
        print("\nВсі нотатки (текст, дата)")
        select_account(conn)
        
 
if __name__ == '__main__':
    main()
