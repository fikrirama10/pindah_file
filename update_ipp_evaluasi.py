import mysql.connector
import datetime
import uuid

config = {
    'user': 'root',
    'password': '#e-Penyiaran@2022!',
    'host': '192.168.1.23',
    'database': 'simp3_v2',
    'raise_on_warnings': True,
    'port': 3360
}

def connect_db():
    try:
        db = mysql.connector.connect(**config)
        print("Database berhasil dihubungi")
        return db
    except mysql.connector.Error as err:
        print("Database gagal dihubungi: {}".format(err))
     
#cek ipp di tabel ipp
def start_():
    db = connect_db()
    cursor = db.cursor()
    sql = "SELECT no_ipp_tetap,tgl_ipp_tetap,tgl_perpanjangan,id_jenis_penyiaran,IDPERUSAHAAN FROM target_evaluasi WHERE IDPERUSAHAAN IS NOT NULL"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        #cek table ipp
        db1 = connect_db()
        cursor1 = db1.cursor()
        sql = "SELECT no_ipp,tgl_mulai,tgl_berakhir FROM ipp WHERE id_jenis_penyiaran='"+str(row[3])+"'"
        cursor1.execute(sql)
        results1 = cursor1.fetchone()
        if results1 == None:
            #create ipp
            db2 = connect_db()
            cursor2 = db2.cursor()
            created_at =  datetime.datetime.now()
            update_at =  datetime.datetime.now()
            uuid_ = uuid.uuid4()
            sql = "INSERT INTO ipp (id,no_ipp,tgl_mulai,tgl_berakhir,id_jenis_penyiaran,created_at,updated_at,jenis_ipp,status_ipp,active) VALUES ('"+str(uuid_)+"','"+str(row[0])+"','"+str(row[1])+"','"+str(row[2])+"','"+str(row[3])+"','"+str(created_at)+"','"+str(update_at)+"','IPP TETAP','permohonan baru','1')"
            cursor2.execute(sql)
            db2.commit()
            print("berhasil create "+str(row[0]))
        else:    
        #update table ipp 
            db2 = connect_db()
            cursor2 = db2.cursor()
            update_at =  datetime.datetime.now()
            sql = "UPDATE ipp SET no_ipp = '"+str(row[0])+"', tgl_mulai= '"+str(row[1])+"', tgl_berakhir= '"+str(row[2])+"' , updated_at='"+str(update_at)+"' WHERE id_jenis_penyiaran = '"+str(row[3])+"'"
            cursor2.execute(sql)
            db2.commit()
            print("berhasil update "+str(row[0]))
            # pass

start_()