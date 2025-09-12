import psycopg2
from cryptography.fernet import Fernet
from psycopg2._psycopg import cursor
import base64
from securepass import encrypt_password, decrypt_password


def dbconnect():
    conn = psycopg2.connect(
        "dbname=passwordstore user=postgres password=password",
        # Hard-coded credentials is bad practice and is only used for simplicity in demonstration
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    return conn, cursor

def dbclose(conn, cursor):
    cursor.close()
    conn.close()

def write_to_table_credentials(values):
    conn, cursor = dbconnect()
    cursor.execute('''
    INSERT INTO credentials (website, username, salt, pass_hash)
    VALUES (%s, %s, %s, %s)''', values) # Code Security: use Parametrized Queries to Prevent SQL injection
    conn.commit()
    dbclose(conn, cursor)

def write_to_table_securedpassword(website, username, password):
    encrypted_password = encrypt_password(password)
    conn, cursor = dbconnect()
    cursor.execute('''
    INSERT INTO securedpasswords (user_id, website, username, encrypted_password)
    VALUES (
        (SELECT user_id FROM credentials WHERE website = %s AND username = %s),  
        %s, %s, %s)''', (website, username, website, username, encrypted_password))
    conn.commit()
    dbclose(conn, cursor)

def retrieve_data(values):
    conn, cursor = dbconnect()
    cursor.execute ('''
    SELECT website, username, pass_hash, salt FROM credentials
    WHERE website = %s AND username = %s''', values)
    data = cursor.fetchall()
    dbclose(conn, cursor)
    return data

def password_recovery(values):
    conn, cursor = dbconnect()
    cursor.execute ('''
    SELECT encrypted_password FROM securedpasswords
    WHERE website = %s AND username = %s''', values)

    data = cursor.fetchall()
    dbclose(conn, cursor)

    return data[0][0]