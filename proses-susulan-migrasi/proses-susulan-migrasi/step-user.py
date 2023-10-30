import uuid

from mysql.connector import connect, Error
import mysql.connector
import requests
import json
from bs4 import BeautifulSoup

config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "simp3_user_v2"
}

def destinantion_connection():
    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            return connection
    except Error as e:
        print("Error while connecting to MySQL", e)

def get_users():
    try:
        connection = destinantion_connection()
        cursor = connection.cursor()
        cursor.execute(" SELECT id, email_asal, idperusahaanfinal FROM users WHERE email_asal = 't7legal.corporate@gmail.com'")
        records = cursor.fetchall()
        return records
    except Error as e:
        print("Error while connecting to MySQL", e)

def main():
    records = get_users()
    for row in records:
        id = row[0]
        email_asal = row[2]
        idpf = row[2]
        email = idpf + "@gmail.com"
        connection2 = destinantion_connection()
        cursor2 = connection2.cursor()
        cursor2.execute("UPDATE users SET  email = %s WHERE id = %s ", (email, id))
        connection2.commit()
        print("Update username berhasil", email)
    else:
            username = None
        


if __name__ == "__main__":
    main()





