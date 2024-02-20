from dbConfig import mysql

def create_user_table_if_not_exists():
    cur = mysql.connection.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            role VARCHAR(50) NOT NULL
        )
    """)
    mysql.connection.commit()
    cur.close()

def create_user(name, email, role):
    create_user_table_if_not_exists() 
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users (name, email, role) VALUES (%s, %s, %s)", (name, email, role))
    mysql.connection.commit()
    user_id = cur.lastrowid
    cur.close()
    return {
        'id': user_id,
        'name': name,
        'email': email,
        'role': role
    }

def get_all_users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    cur.close()
    return users

def get_user(user_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cur.fetchone()
    cur.close()
    return user
