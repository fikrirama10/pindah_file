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

def lampiranfile():
    connection = destinantion_connection()
    cursor = connection.cursor()
    sql = "SELECT jenis_penyiaran.id_asal, jenis_penyiaran.idperusahaanfinal_origin,pengajuan_ulop_radio.id FROM jenis_penyiaran LEFT JOIN pengajuan_ulop_radio ON jenis_penyiaran.id = pengajuan_ulop_radio.id_penyiaran"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def start_():
    list_ = lampiranfile()
    for i in list_:
        id_ = i[0]
        idperusahaanfinal_origin = i[1]
        id = i[2]
        connection = source_connection()
        cursor = connection.cursor()
        sql = "SELECT DISTINCT field_name, file_name, id_ref FROM lampiranfile WHERE origin_type = 'lampiran' AND id_ref = %s"
        cursor.execute(sql, (id_,))
        result = cursor.fetchall()
        for j in result:
            field_name = j[0]
            file_name = j[1]
            id_ref = j[2]
            #SURAT_ULOP to file_permohonan_ulop
            #SCAN_DOKUMEN_ISR to file_dokumen_isr
            #DOKUMEN_ULO to file_dokumen_ulop
          
           
            connection2 = destinantion_connection()
            cursor2 = connection2.cursor()
            
            if field_name == 'SURAT_ULOP':
                # update field file_scan_ipp di tabel pengajuan_ulop_tv berdasarkan id
                sql2 = "UPDATE pengajuan_ulop_radio SET file_permohonan_ulop = %s WHERE id = %s"
                cursor2.execute(sql2, (file_name, id,))
                connection2.commit()
                print("record updated.",file_name, id)
                
            elif field_name == 'SCAN_DOKUMEN_ISR':
                # update field file_scan_isr di tabel pengajuan_ulop_tv berdasarkan id
                sql2 = "UPDATE pengajuan_ulop_radio SET file_dokumen_isr = %s WHERE id = %s"
                cursor2.execute(sql2, (file_name, id,))
                connection2.commit()
                print("record updated.",file_name, id)
                
            elif field_name == 'DOKUMEN_ULO':
                # update field file_aspek_managemen di tabel pengajuan_ulop_tv berdasarkan id
                sql2 = "UPDATE pengajuan_ulop_radio SET file_dokumen_ulop = %s WHERE id = %s"
                cursor2.execute(sql2, (file_name, id,))
                connection2.commit()
                print("record updated.",file_name, id)
                                
           
            else:
                print('tidak ada')

       

def main():
    start_()


if __name__ == "__main__":
    main()
