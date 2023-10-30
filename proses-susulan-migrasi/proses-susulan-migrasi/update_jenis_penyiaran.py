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
    sql = "SELECT idperusahaanfinal_origin FROM jenis_penyiaran "
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def start_():
    list_ = get_data_wilayah_source()
    for i in list_:
        id = i[0]
        connection = source_connection()
        cursor = connection.cursor()
        sql = "SELECT tgl_pleno, tgl_pengajuan,tgl_evaluasi FROM tbl_eucs WHERE id_perusahaan = %s"
        cursor.execute(sql, (id,))
        result = cursor.fetchone()
        if result is not None:
            tgl_pleno = result[0]
            tgl_pengajuan = result[1]
            tgl_evaluasi = result[2]
            connection = destinantion_connection()
            cursor = connection.cursor()
            sql = "UPDATE jenis_penyiaran SET tgl_verifikasi_registrasi = %s, created_at = %s, updated_at = %s, tgl_submit= %s WHERE idperusahaanfinal_origin = %s"
            cursor.execute(sql, (tgl_pleno, tgl_pengajuan, tgl_evaluasi,tgl_pengajuan, id))
            connection.commit()
            print("record updated.",tgl_pleno, tgl_pengajuan, tgl_evaluasi, id)
       

def main():
    start_()


if __name__ == "__main__":
    main()
