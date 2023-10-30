import uuid

from mysql.connector import connect, Error
import mysql.connector


# Informatsi koneksi MySQL Destinasi
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

def get_data_wilayah_source():
    connection = destinantion_connection()
    cursor = connection.cursor()
    sql = "SELECT * FROM riwayat_jenis_penyiaran WHERE status > 6"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def start_():
    list_ = get_data_wilayah_source()
    for i in list_:
        id = i[0]
        jenis_permohonan = 'perpanjangan'
        ipp_ke = 2
        connection = destinantion_connection()
        cursor = connection.cursor()
        sql = "UPDATE riwayat_jenis_penyiaran SET jenis_permohonan = %s, ipp_ke= %s WHERE id = %s"
        cursor.execute(sql, (jenis_permohonan, ipp_ke, id,))
        connection.commit()
        print("record updated.",jenis_permohonan, ipp_ke, id)
       

def main():
    start_()


if __name__ == "__main__":
    main()
