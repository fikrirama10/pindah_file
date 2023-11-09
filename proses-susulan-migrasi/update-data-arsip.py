import uuid

from mysql.connector import connect, Error
import mysql.connector
from datetime import datetime

# Informatsi koneksi MySQL Destinasi
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    # 'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
    'database': 'simp3_user_v2',
    'raise_on_warnings': True,
    'port': 3306
}
# config = {
#     'user': 'root',
#     'password': '#e-Penyiaran@2022!',
#     'host': '192.168.1.23',
#     # 'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
#     'database': 'simp3_v2',
#     'raise_on_warnings': True,
#     'port': 3360
# }

config2 = {
    'user': 'root',
    'password': '#e-Penyiaran@2022!',
    'host': '192.168.1.23',
    # 'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
    'database': 'simp3_db_golive',
    'raise_on_warnings': True,
    'port': 3360
}

def destinantion_connection():
    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            db_Info = connection.get_server_info()
            # print("Connected to MySQL Server version ", db_Info)
            return connection
    except Error as e:
        print("Error while connecting to MySQL", e)


def source_connection():
    try:
        connection = mysql.connector.connect(**config2)
        if connection.is_connected():
            db_Info = connection.get_server_info()
            # print("Connected to MySQL Server version ", db_Info)
            return connection
    except Error as e:
        print("Error while connecting to MySQL", e)

def main():
    #koneksi ke database destinasi
    connection = destinantion_connection()
    cursor = connection.cursor()
    #koneksi ke database source
    connection2 = source_connection()
    cursor2 = connection2.cursor()
    #query select data dari database source
    query = "SELECT IDPERUSAHAANFINAL FROM users WHERE active = 0 AND IDPERUSAHAANFINAL IS NOT NULL"
    cursor2.execute(query)
    result = cursor2.fetchall()
    for row in result:
        # print(row)
        # print(row[0])
        # print(uuid.UUID(row[0]))
        update_at = datetime.now()
        query2 = "UPDATE jenis_penyiaran SET status_registrasi = %s,updated_at=%s WHERE idperusahaanfinal_origin = %s"
        cursor.execute(query2, (11,update_at,row[0]))
        connection.commit()
        print(cursor.rowcount, "record(s) affected "+str(row[0]))

main()