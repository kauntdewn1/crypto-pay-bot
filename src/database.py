import sqlite3

def connect_db():
    """Estabelece a conexão com o banco de dados SQLite."""
    conn = sqlite3.connect('database.db')
    return conn

def create_tables():
    """Cria a tabela de transações se ela não existir."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL,
            currency TEXT,
            status TEXT
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
