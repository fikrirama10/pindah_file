#koneksi ke simp3_db_golive
import mysql.connector

config = {
    'user': 'root',
    'password': '#e-Penyiaran@2022!',
    'host': '192.168.1.23',
    'database': 'simp3_v2',
    'raise_on_warnings': True,
    'port': 3360
}

config_golive = {
    'user': 'root',
    'password': '#e-Penyiaran@2022!',
    'host': '192.168.1.23',
    'database': 'simp3_db_golive',
    'raise_on_warnings': True,
    'port': 3360
}
#fungsi untuk koneksi ke database
def connect_db():
    try:
        db = mysql.connector.connect(**config)
        print("Database berhasil dihubungi")
        return db
    except mysql.connector.Error as err:
        print("Database gagal dihubungi: {}".format(err))

#fungsi untuk koneksi ke database config golive
def connect_db_golive():
    try:
        db = mysql.connector.connect(**config_golive)
        print("Database berhasil dihubungi")
        return db
    except mysql.connector.Error as err:
        print("Database gagal dihubungi: {}".format(err))

def cek_nama_perusahaan(nama):
    db = connect_db_golive()
    cursor = db.cursor()
    sql = "SELECT IDPERUSAHAANFINAL,NMPERUSAHAAN FROM penyelenggara WHERE NMPERUSAHAAN LIKE '%" + str(nama) + "%'"
    cursor.execute(sql)
    results = cursor.fetchone()
    if results is None:
        pass
    else:
        #update IDPERUSAHAAN DI TABEL target_evaluasi
        db2 = connect_db()
        cursor2 = db2.cursor()
        sql = "UPDATE tahapan_kebijakan SET id_perusahaan = '"+str(results[0])+"' WHERE nm_perusahaan = '"+str(nama)+"'"
        cursor2.execute(sql)
        db2.commit()

def start_():
    db = connect_db()
    cursor = db.cursor()
    sql = "SELECT nm_perusahaan FROM tahapan_kebijakan WHERE id_perusahaan IS NULL"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        nama = row[0]
        data = cek_nama_perusahaan(nama)
        print(data)

start_()