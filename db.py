import psycopg2

def connect():
    try:
        conn = psycopg2.connect(
        host="db",
        database="test_db",
        user="root",
        password="root")
    except Exception as e:
        print(e)
        exit(0)
    return conn

def create_db():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (chat_id integer, source text, result text)')
    conn.commit()
    conn.close()

def insert_into(chat_id, source, result):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(f'INSERT INTO users(chat_id, source, result) VALUES ({chat_id}, \'{source}\', \'{result}\')')
    conn.commit()
    conn.close()