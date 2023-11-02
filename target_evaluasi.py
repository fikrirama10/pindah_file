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
#fungsi cek tbl_ipp_prinsip
def cek_ipp_prinsip(id):
    db = connect_db_golive()
    cursor = db.cursor()
    sql = "SELECT no_ipp_prinsip,tgl_ipp_prinsip,tgl_perpanjangan FROM tbl_ipp_prinsip WHERE id_perusahaan='"+str(id)+"'"
    cursor.execute(sql)
    results = cursor.fetchone()
    if results is None:
        pass
    else:
        #update target_evaluasi set no_ipp_prinsip = 'no_ipp_prinsip', tgl_ipp_prinsip = 'tgl_ipp_prinsip', tgl_perpanjangan_prinsip = 'tgl_perpanjangan' where idperusahaan = 'id'
        db2 = connect_db()
        cursor2 = db2.cursor()
        sql = "UPDATE target_evaluasi SET no_ipp_prinsip = '"+str(results[0])+"', tgl_ipp_prinsip = '"+str(results[1])+"', tgl_perpanjangan_prinsip = '"+str(results[2])+"' WHERE IDPERUSAHAAN = '"+str(id)+"'"
        cursor2.execute(sql)
        db2.commit()
        
    return results

#fungsi cek nama_perusahaan di tabel penyelenggara config
def cek_nama_perusahaan(nama):
    db = connect_db_golive()
    cursor = db.cursor()
    sql = "SELECT NMPERUSAHAAN FROM penyelenggara WHERE NMPERUSAHAAN LIKE '%" + str(nama) + "%'"
    cursor.execute(sql)
    results = cursor.fetchone()
    if results is None:
        pass
    else:
        #update IDPERUSAHAAN DI TABEL target_evaluasi
        db2 = connect_db()
        cursor2 = db2.cursor()
        sql = "UPDATE target_evaluasi SET IDPERUSAHAAN = '"+str(results[0])+"' WHERE NAMA = '"+str(nama)+"'"
        cursor2.execute(sql)
        db2.commit()

    return results
#cek ipp_tetap di zzhitoris
def cek_ipp_tetap_zzhitoris(id):
    db = connect_db_golive()
    cursor = db.cursor()
    sql = "SELECT no_ipp_tetap,tgl_ipp_tetap,tgl_perpanjangan FROM zzhistoris_tbl_ipp_tetap WHERE id_perusahaan='"+str(id)+"'"
    cursor.execute(sql)
    results = cursor.fetchone()
    if results is None:
        results = cek_ipp_prinsip(id)
        return results
    else:
        #update target_evaluasi set no_ipp_tetap = 'no_ipp_tetap', tgl_ipp_tetap = 'tgl_ipp_tetap', tgl_perpanjangan = 'tgl_perpanjangan' where idperusahaan = 'id'
        db2 = connect_db()
        cursor2 = db2.cursor()
        sql = "UPDATE target_evaluasi SET no_ipp_tetap = '"+str(results[0])+"', tgl_ipp_tetap = '"+str(results[1])+"', tgl_perpanjangan = '"+str(results[2])+"' WHERE IDPERUSAHAAN = '"+str(id)+"'"
        cursor2.execute(sql)
        db2.commit()
        
    return results

#fungsi cek ipp_Tetap
def cek_ipp_tetap(id):
    db = connect_db_golive()
    cursor = db.cursor()
    # sql = "SELECT no_ipp_tetap,tgl_ipp_tetap,tgl_perpanjangan FROM tbl_ipp_tetap WHERE id_perusahaan='RS201602390' ORDER BY id_ipp_tetap ASC"
    sql = "SELECT no_ipp_tetap,tgl_ipp_tetap,tgl_perpanjangan FROM tbl_ipp_tetap WHERE id_perusahaan='"+str(id)+"'"
    cursor.execute(sql)
    results = cursor.fetchone()
    if results is None:
        results = cek_ipp_tetap_zzhitoris(id)
        return results
    else:
        db2 = connect_db()
        cursor2 = db2.cursor()
        #update target_evaluasi set no_ipp_tetap = 'no_ipp_tetap', tgl_ipp_tetap = 'tgl_ipp_tetap', tgl_perpanjangan = 'tgl_perpanjangan' where idperusahaan = 'id'
        sql = "UPDATE target_evaluasi SET no_ipp_tetap = '"+str(results[0])+"', tgl_ipp_tetap = '"+str(results[1])+"', tgl_perpanjangan = '"+str(results[2])+"' WHERE IDPERUSAHAAN = '"+str(id)+"'"
        cursor2.execute(sql)
        db2.commit()
        return results

def cek_status_evaluasi(id):
    db = connect_db_golive()
    cursor = db.cursor()
    # sql = "SELECT no_ipp_tetap,tgl_ipp_tetap,tgl_perpanjangan FROM tbl_ipp_tetap WHERE id_perusahaan='RS201602390' ORDER BY id_ipp_tetap ASC"
    sql = "SELECT keputusan_perpanjangan_subdit,tgl_ba_subdit FROM vw_berita_acara WHERE IDPERUSAHAANFINAL = '"+str(id)+"' AND tgl_ba_subdit IS NOT NULL"
    cursor.execute(sql)
    results = cursor.fetchone()
    if results == None:
        pass
    else:
        # return results
        #update target evaluasi
        db2 = connect_db()
        cursor2 = db2.cursor()
        #update target_evaluasi set no_ipp_tetap = 'no_ipp_tetap', tgl_ipp_tetap = 'tgl_ipp_tetap', tgl_perpanjangan = 'tgl_perpanjangan' where idperusahaan = 'id'
        sql = "UPDATE target_evaluasi SET status_evaluasi = '"+str(results[0])+"', tgl_evaluasi = '"+str(results[1])+"' WHERE IDPERUSAHAAN = '"+str(id)+"'"
        cursor2.execute(sql)
        db2.commit()
        return id
#fungsi get id_jenis_penyiaran di table jenis_penyiaran
def get_id_jenis_penyiaran(id):
    db = connect_db()
    cursor = db.cursor()
    sql = "SELECT id,idperusahaanfinal_origin FROM jenis_penyiaran WHERE idperusahaanfinal_origin = '"+str(id)+"'"
    cursor.execute(sql)
    results = cursor.fetchone()
    if results is None:
        pass
    else:
        #update id_jenis_penyiaran di table target_evaluasi
        db2 = connect_db()
        cursor2 = db2.cursor()
        sql = "UPDATE target_evaluasi SET id_jenis_penyiaran = '"+str(results[0])+"' WHERE IDPERUSAHAAN = '"+str(id)+"'"
        cursor2.execute(sql)
        db2.commit()
    return results

def start_():
    db = connect_db()
    cursor = db.cursor()
    sql = "SELECT IDPERUSAHAAN,NAMA FROM target_evaluasi WHERE IDPERUSAHAAN IS NOT NULL"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        id = row[0]
        # print(id)
        status = cek_status_evaluasi(id)
        idpenyiaran = get_id_jenis_penyiaran(id)
        # print(idpenyiaran)
        if id == None:
            nama = row[1]
            data = cek_nama_perusahaan(nama)
        else:
            data = cek_ipp_tetap(id)
            print(str(data)+'-'+str(id))

start_()