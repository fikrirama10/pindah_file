#koneksi ke simp3_db_golive
import mysql.connector
from datetime import datetime

config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'simp3_user_v2',
    # 'raise_on_warnings': True,
    'port': 3306
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

def sklo_radio(id):
    # print(str(id)+'radio')
    #update no_sklo di table pengajuan_ulop_radio
    db = connect_db_golive()
    cursor = db.cursor()
    query = """
   SELECT
        tbl_frb.id_perusahaan,
        tbl_frb.no_surat,
        tbl_frb.tgl_berita_acara
    FROM tbl_frb
    INNER JOIN penyelenggara ON penyelenggara.IDPERUSAHAANFINAL = tbl_frb.id_perusahaan
    WHERE tbl_frb.no_surat IS NOT NULL   
    AND tbl_frb.id_perusahaan = %s
    """

    # Eksekusi query dengan parameter
    id_perusahaan = id  # Ganti dengan nilai ID yang sesuai
    cursor.execute(query, (id_perusahaan,))
    results = cursor.fetchone()
    if results is None:
        pass
    else:
        #select jenis_penyiaran where idperusahaanfinal_origin = id
        db2 = connect_db()
        cursor2 = db2.cursor()
        sql = "SELECT id FROM jenis_penyiaran WHERE idperusahaanfinal_origin = '"+str(id)+"' AND kategori_siaran = 'radio'"
        cursor2.execute(sql)
        results2 = cursor2.fetchone()
        if results2 is None:
            pass
        else:
        #update pengajuan ulop
            db3 = connect_db()
            cursor3 = db3.cursor()
            update_at = datetime.now()
            sql = "UPDATE pengajuan_ulop_radio SET status_ulo=5, tgl_verifikasi_ulo='"+str(results[2])+"', no_sklo = '"+str(results[1])+"' ,updated_at='"+str(update_at)+"' WHERE id_penyiaran = '"+str(results2[0])+"'"
            cursor3.execute(sql)
            db3.commit()
            print('berhasil sklo radio')
    return results
    
def start_():
    db = connect_db_golive()
    cursor = db.cursor()
    query = """
    SELECT
        tbl_frb.id_perusahaan,
        penyelenggara.NMPERUSAHAAN,
        tbl_frb.no_surat,
        tbl_frb.tgl_berita_acara
    FROM tbl_frb
    INNER JOIN penyelenggara ON penyelenggara.IDPERUSAHAANFINAL = tbl_frb.id_perusahaan
    WHERE tbl_frb.no_surat IS NOT NULL
    GROUP BY tbl_frb.id_perusahaan
    """
    cursor.execute(query)

    # Ambil hasil query 
    results = cursor.fetchall()
    for row in results:
    #    sklo_tv_ =  sklo_tv(row[0])
       sklo_radio_ =  sklo_radio(row[0])

       print(str(sklo_radio_))


start_()