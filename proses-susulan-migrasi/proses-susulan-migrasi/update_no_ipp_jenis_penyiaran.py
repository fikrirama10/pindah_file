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
    sql = "SELECT idperusahaanfinal_origin, id FROM jenis_penyiaran "
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def start_():
    list_ = get_data_wilayah_source()
    for i in list_:
        id = i[0]
        id_jenis_penyiaran = i[1]
        connection = destinantion_connection()
        cursor = connection.cursor()
        sql = "SELECT no_ipp_tetap FROM target_tahapan WHERE IDPERUSAHAANFINAL = %s"
        cursor.execute(sql, (id,))
        result = cursor.fetchone()
        if result is not None:
            no_ipp_tetap = result[0]
            connection = destinantion_connection()
            cursor = connection.cursor()
            sql = "UPDATE jenis_penyiaran SET nomer_ipp_aktif = %s WHERE idperusahaanfinal_origin = %s"
            cursor.execute(sql, (no_ipp_tetap,id))
            connection.commit()
            print("record jenis_penyiaran.",no_ipp_tetap,id)
            sql2 = "UPDATE ipp SET no_ipp = %s WHERE id_jenis_penyiaran = %s"
            cursor.execute(sql2, (no_ipp_tetap,id_jenis_penyiaran))
            print("record ipp.",no_ipp_tetap,id)
       

def main():
    start_()


if __name__ == "__main__":
    main()
