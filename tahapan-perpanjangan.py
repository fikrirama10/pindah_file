import shutil
from mysql.connector import connect, Error
import mysql.connector
import uuid
from datetime import datetime

# config = {
#     'user': 'root',
#     'password': '',
#     'host': 'localhost',
#     # 'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
#     'database': 'simp3_user_v2',
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


def destinantion_connection():
    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            return connection
    except Error as e:
        print("Error while connecting to MySQL", e)

def get_perusahaan(id):
    connection = destinantion_connection()
    cursor = connection.cursor()
    cursor.execute(" SELECT id from jenis_penyiaran  where idperusahaanfinal_origin = '"+id+"'  ")
    records = cursor.fetchone()
    return records[0]

def update_ipp(id_penyiaran,id_perusahaan):
    connection = destinantion_connection()
    cursor = connection.cursor()
    cursor.execute(" SELECT * from vw_berita_acara WHERE IDPERUSAHAANFINAL = '"+id_perusahaan+"' ")
    records = cursor.fetchone()
    if records:
        tgl_mulai = records[13]
        tgl_berakhir = records[14]
        no_ipp = records[10]
        id = id_penyiaran
        update_at = datetime.now()
        connection2 = destinantion_connection()
        cursor2 = connection2.cursor()
        cursor2.execute("UPDATE ipp SET  no_ipp = %s , tgl_mulai =%s, tgl_berakhir=%s , updated_at=%s  WHERE id_jenis_penyiaran = %s ", (no_ipp,tgl_mulai,tgl_berakhir,update_at, id))
        connection2.commit()
        print("Update berhasil", str(id_perusahaan))

def tes():
    connection = destinantion_connection()
    cursor = connection.cursor()
    conn2 = destinantion_connection()
    cursor2 = conn2.cursor()
    cursor.execute(" SELECT * from vw_berita_acara")
    records = cursor.fetchall()
    
    for row in records:
        connection2 = destinantion_connection()
        cek_perusahaan = connection2.cursor()
        cek_perusahaan.execute("SELECT idperusahaanfinal_origin,jenis_penyiaran.id from jenis_penyiaran JOIN perpanjangan ON perpanjangan.id_penyiaran = jenis_penyiaran.id where idperusahaanfinal_origin = '"+row[1]+"'")
        idperusahaan_ = cek_perusahaan.fetchone()
        if idperusahaan_ == None:
           myuuid = uuid.uuid4()
           perusahaan = get_perusahaan(row[1])
           #create perpanjangan
        #    id = str(myuuid)
           id_penyiaran = str(perusahaan)
        #    id_status = str(row[20])
        #    tgl_evaluasi = str(row[16])
        #    tgl_perpanjangan = str(row[14])
        #    proses = 1
           
        #    data_insert = (id,id_penyiaran,id_status,tgl_evaluasi,tgl_perpanjangan,proses)
        #    query_insert = """ INSERT INTO perpanjangan(id,id_penyiaran,id_status,tgl_evaluasi,tgl_perpanjangan,proses) VALUES (%s, %s, %s, %s, %s, %s) """
        #    cursor2.execute(query_insert, data_insert)
        #    conn2.commit()
        #    print("insert berhasil "+str(id))
           update_ipp(id_penyiaran,row[1])
          
        else:
            update_ipp(idperusahaan_[1],idperusahaan_[0])
            print("update berhasil")

tes()