import uuid

from mysql.connector import connect, Error
import mysql.connector
from datetime import datetime

# Informatsi koneksi MySQL Destinasi
# config = {
#     'user': 'root',
#     'password': '',
#     'host': 'localhost',
#     # 'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
#     'database': 'simp3_user_v2',
#     'raise_on_warnings': True,
#     'port': 3306
# }
config = {
    'user': 'root',
    'password': '#e-Penyiaran@2022!',
    'host': '192.168.1.23',
    # 'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
    'database': 'simp3_v2',
    'raise_on_warnings': True,
    'port': 3360
}

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

#get tbl_pengecekan from source connection where tgl_dok_subditradio is not null
def get_data_from_source():
    try:
        connection = source_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM tbl_pengecekan where tgl_dok_subditradio is not null")
        records = cursor.fetchall()
        return records
    except Error as e:
        print("Error while connecting to MySQL", e)

#get_idperusahaanfinal_destination
def get_idperusahaanfinal_destination(idperusahaanfinal_origin):
    try:
        connection = destinantion_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT idperusahaanfinal_origin FROM jenis_penyiaran where idperusahaanfinal_origin = %s", (idperusahaanfinal_origin,))
        records = cursor.fetchone()
        # print(str(records[0])+' data ditemukan')
        if records is None:
            print("idperusahaanfinal_origin tidak ditemukan")
            return None
        return records[0]

    except Error as e:
        print("Error while connecting to MySQL", e)
#update status_registrasi tidak lengkap
def update_status_registrasi_tidak_lengkap(idperusahaanfinal_destination):
    try:
        connection = destinantion_connection()
        cursor = connection.cursor()
        cursor.execute("UPDATE jenis_penyiaran SET status_registrasi = 4 WHERE idperusahaanfinal_origin = %s", (idperusahaanfinal_destination,))
        connection.commit()
        #print berhasil
        print("berhasil update status_registrasi tidak lengkap")
    except Error as e:
        print("Error while connecting to MySQL", e)

def update_status_registrasi_lengkap(idperusahaanfinal_destination):
    try:
        connection = destinantion_connection()
        cursor = connection.cursor()
        cursor.execute("UPDATE jenis_penyiaran SET status_registrasi = 3 WHERE idperusahaanfinal_origin = %s", (idperusahaanfinal_destination,))
        connection.commit()
        #print berhasil
        print("berhasil update status_registrasi lengkap")
    except Error as e:
        print("Error while connecting to MySQL", e)

#update tgl_verifikasi_registrasi
def update_tgl_dok_subditradio(idperusahaanfinal_destination,tgl_dok_subditradio):
    try:
        connection = destinantion_connection()
        cursor = connection.cursor()
        cursor.execute("UPDATE jenis_penyiaran SET tgl_verifikasi_registrasi = %s WHERE idperusahaanfinal_origin = %s", (tgl_dok_subditradio,idperusahaanfinal_destination,))
        connection.commit()
        #print berhasil
        print("berhasil update tgl_verifikasi_registrasi")
    except Error as e:
        print("Error while connecting to MySQL", e)

def main():
    #get_data
    data = get_data_from_source()
    #looping data
    for row in data:
        #get idperusahaanfinal_origin
        idperusahaanfinal_origin = row[2]
        #get tgl_dok_subditradio
        tgl_dok_subditradio = row[9]
        #get status_dok_subditradio
        status_dok_subditradio = row[8]
        #get idperusahaanfinal_destination
        idperusahaanfinal_destination = get_idperusahaanfinal_destination(idperusahaanfinal_origin)
        #update tgl_dok_subditradio
        if idperusahaanfinal_destination is not None:
            update_tgl_dok_subditradio(idperusahaanfinal_destination,tgl_dok_subditradio)
            if status_dok_subditradio == 2:
                update_status_registrasi_tidak_lengkap(idperusahaanfinal_destination)
            elif status_dok_subditradio == 1:
                update_status_registrasi_lengkap(idperusahaanfinal_destination)
            else:
                pass
        else:
            pass
    #update jenis_penyiaran from destination where idperusahaanfinal_origin
   


main()