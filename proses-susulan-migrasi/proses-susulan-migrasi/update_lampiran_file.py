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
    sql = "SELECT DISTINCT jenis_penyiaran.id_asal, jenis_penyiaran.idperusahaanfinal_origin FROM jenis_penyiaran JOIN lampiran_penyiaran ON lampiran_penyiaran.idperusahaanfinal_origin = jenis_penyiaran.idperusahaanfinal_origin"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def start_():
    list_ = lampiranfile()
    for i in list_:
        id = i[0]
        idperusahaanfinal_origin = i[1]
        connection = source_connection()
        cursor = connection.cursor()
        sql = "SELECT DISTINCT field_name, file_name, id_ref FROM lampiranfile WHERE origin_type = 'lampiran' AND id_ref = %s"
        cursor.execute(sql, (id,))
        result = cursor.fetchall()
        for j in result:
            field_name = j[0]
            file_name = j[1]
            id_ref = j[2]
            #SCAN_IPP_TERAKHIR to file_scan_ipp
            #SCAN_DOKUMEN_ISR to file_scan_isr
            #STRUKTUR_ORGANISASI to file_aspek_managemen
            # SALINAN_AKTA_PENDIRIAN  to file_akta_pendirian
            # SALINAN_AKTA_PERUBAHAN to file_akta_perubahan
            # PKS_MUX to file_pks_mux 
            # SUSUNAN_PENGURUS to file_akta_pengurus
            # PERNYATAAN_KEBENARAN_DATA to file_surat_pernyataan
            # DUKUNGAN to dukungan_tertulis
            # FOTOKOPI_BERKAS_REKOMENDASI to foto_rekomendasi
            # SALINAN_PENGESAHAN_AKTA to file_akta_pengesahan_pendirian
            # SALINAN_PENGESAHAN_AKTA_PERUBAHAN to file_akta_pengesahan_perubahan
            # FOTOKOPI_NPWP to file_fotokopi_npwp
            connection2 = destinantion_connection()
            cursor2 = connection2.cursor()
            
            if field_name == 'SCAN_IPP_TERAKHIR':
                # update field file_scan_ipp di tabel lampiran_penyiaran berdasarkan id_perusahaanfinal_origin
                sql2 = "UPDATE lampiran_penyiaran SET file_scan_ipp = %s WHERE idperusahaanfinal_origin = %s"
                cursor2.execute(sql2, (file_name, idperusahaanfinal_origin,))
                connection2.commit()
                print("record updated.",file_name, idperusahaanfinal_origin)
                
            # elif field_name == 'SCAN_DOKUMEN_ISR':
            #     # update field file_scan_isr di tabel lampiran_penyiaran berdasarkan id_perusahaanfinal_origin
            #     sql2 = "UPDATE lampiran_penyiaran SET file_scan_isr = %s WHERE idperusahaanfinal_origin = %s"
            #     cursor2.execute(sql2, (file_name, idperusahaanfinal_origin,))
            #     connection2.commit()
            #     print("record updated.",file_name, idperusahaanfinal_origin)
                
            # elif field_name == 'STRUKTUR_ORGANISASI':
            #     # update field file_aspek_managemen di tabel lampiran_penyiaran berdasarkan id_perusahaanfinal_origin
            #     sql2 = "UPDATE lampiran_penyiaran SET file_aspek_managemen = %s WHERE idperusahaanfinal_origin = %s"
            #     cursor2.execute(sql2, (file_name, idperusahaanfinal_origin,))
            #     connection2.commit()
            #     print("record updated.",file_name, idperusahaanfinal_origin)
                
            # elif field_name == 'SALINAN_AKTA_PENDIRIAN':
            #     # update field file_akta_pendirian di tabel lampiran_penyiaran berdasarkan id_perusahaanfinal_origin
            #     sql2 = "UPDATE lampiran_penyiaran SET file_akta_pendirian = %s WHERE idperusahaanfinal_origin = %s"
            #     cursor2.execute(sql2, (file_name, idperusahaanfinal_origin,))
            #     connection2.commit()
            #     print("record updated.",file_name, idperusahaanfinal_origin)
                
            # elif field_name == 'SALINAN_AKTA_PERUBAHAN':
            #     # update field file_akta_perubahan di tabel lampiran_penyiaran berdasarkan id_perusahaanfinal_origin
            #     sql2 = "UPDATE lampiran_penyiaran SET file_akta_perubahan = %s WHERE idperusahaanfinal_origin = %s"
            #     cursor2.execute(sql2, (file_name, idperusahaanfinal_origin,))
            #     connection2.commit()
            #     print("record updated.",file_name, idperusahaanfinal_origin)
                
            # elif field_name == 'PKS_MUX':
            #     # update field file_pks_mux di tabel lampiran_penyiaran berdasarkan id_perusahaanfinal_origin
            #     sql2 = "UPDATE lampiran_penyiaran SET file_pks_mux = %s WHERE idperusahaanfinal_origin = %s"
            #     cursor2.execute(sql2, (file_name, idperusahaanfinal_origin,))
            #     connection2.commit()
            #     print("record updated.",file_name, idperusahaanfinal_origin)
                
            # elif field_name == 'SUSUNAN_PENGURUS':
            #     # update field file_akta_pengurus di tabel lampiran_penyiaran berdasarkan id_perusahaanfinal_origin
            #     sql2 = "UPDATE lampiran_penyiaran SET file_akta_pengurus = %s WHERE idperusahaanfinal_origin = %s"
            #     cursor2.execute(sql2, (file_name, idperusahaanfinal_origin,))
            #     connection2.commit()
            #     print("record updated.",file_name, idperusahaanfinal_origin)
                
            # elif field_name == 'PERNYATAAN_KEBENARAN_DATA':
            #     # update field file_surat_pernyataan di tabel lampiran_penyiaran berdasarkan id_perusahaanfinal_origin
            #     sql2 = "UPDATE lampiran_penyiaran SET file_surat_pernyataan = %s WHERE idperusahaanfinal_origin = %s"
            #     cursor2.execute(sql2, (file_name, idperusahaanfinal_origin,))
            #     connection2.commit()
            #     print("record updated.",file_name, idperusahaanfinal_origin)
            
            # elif field_name == 'DUKUNGAN':
            #     # update field dukungan_tertulis di tabel lampiran_penyiaran berdasarkan id_perusahaanfinal_origin
            #     sql2 = "UPDATE lampiran_penyiaran SET dukungan_tertulis = %s WHERE idperusahaanfinal_origin = %s"
            #     cursor2.execute(sql2, (file_name, idperusahaanfinal_origin,))
            #     connection2.commit()
            #     print("record updated.",file_name, idperusahaanfinal_origin)
                
            # elif field_name == 'FOTOKOPI_BERKAS_REKOMENDASI':
            #     # update field foto_rekomendasi di tabel lampiran_penyiaran berdasarkan id_perusahaanfinal_origin
            #     sql2 = "UPDATE lampiran_penyiaran SET foto_rekomendasi = %s WHERE idperusahaanfinal_origin = %s"
            #     cursor2.execute(sql2, (file_name, idperusahaanfinal_origin,))
            #     connection2.commit()
            #     print("record updated.", file_name, idperusahaanfinal_origin)
                
            # elif field_name == 'SALINAN_PENGESAHAN_AKTA':
            #     # update field file_akta_pengesahan_pendirian di tabel lampiran_penyiaran berdasarkan id_perusahaanfinal_origin
            #     sql2 = "UPDATE lampiran_penyiaran SET file_akta_pengesahan_pendirian = %s WHERE idperusahaanfinal_origin = %s"
            #     cursor2.execute(sql2, (file_name, idperusahaanfinal_origin, ))
            #     connection2.commit()
            #     print("record updated.", file_name, idperusahaanfinal_origin)
                
            # elif field_name == 'SALINAN_PENGESAHAN_AKTA_PERUBAHAN':
            #     # update field file_akta_pengesahan_perubahan di tabel lampiran_penyiaran berdasarkan id_perusahaanfinal_origin
            #     sql2 = "UPDATE lampiran_penyiaran SET file_akta_pengesahan_perubahan = %s WHERE idperusahaanfinal_origin = %s"
            #     cursor2.execute(sql2, (file_name, idperusahaanfinal_origin, ))
            #     connection2.commit()
            #     print("record updated.", file_name, idperusahaanfinal_origin)
                
            # elif field_name == 'FOTOKOPI_NPWP':
            #     # update field file_fotokopi_npwp di tabel lampiran_penyiaran berdasarkan id_perusahaanfinal_origin
            #     sql2 = "UPDATE lampiran_penyiaran SET file_fotokopi_npwp = %s WHERE idperusahaanfinal_origin = %s"
            #     cursor2.execute(sql2, (file_name, idperusahaanfinal_origin, ))
            #     connection2.commit()
            #     print("record updated.", file_name, idperusahaanfinal_origin)

            # elif field_name == 'DUKUNGAN':
            #     # update field file_fotokopi_npwp di tabel lampiran_penyiaran berdasarkan id_perusahaanfinal_origin
            #     sql2 = "UPDATE lampiran_penyiaran SET dukungan_tertulis = %s WHERE idperusahaanfinal_origin = %s"
            #     cursor2.execute(sql2, (file_name, idperusahaanfinal_origin, ))
            #     connection2.commit()
            #     print("record updated.", file_name, idperusahaanfinal_origin)
            
            # elif field_name == 'FOTOKOPI_BERKAS_REKOMENDASI':
            #     # update field file_fotokopi_npwp di tabel lampiran_penyiaran berdasarkan id_perusahaanfinal_origin
            #     sql2 = "UPDATE lampiran_penyiaran SET foto_rekomendasi = %s WHERE idperusahaanfinal_origin = %s"
            #     cursor2.execute(sql2, (file_name, idperusahaanfinal_origin, ))
            #     connection2.commit()
            #     print("record updated.", file_name, idperusahaanfinal_origin)

            # elif field_name == 'SPESIFIKASI_TEKNIK':
            #     # update field file_fotokopi_npwp di tabel lampiran_penyiaran berdasarkan id_perusahaanfinal_origin
            #     sql2 = "UPDATE lampiran_penyiaran SET file_rencana_konfirgurasi = %s WHERE idperusahaanfinal_origin = %s"
            #     cursor2.execute(sql2, (file_name, idperusahaanfinal_origin, ))
            #     connection2.commit()
            #     print("record updated.", file_name, idperusahaanfinal_origin)

            # elif field_name == 'LAMPIRAN_NIB':
            #     # update field file_fotokopi_npwp di tabel lampiran_penyiaran berdasarkan id_perusahaanfinal_origin
            #     sql2 = "UPDATE lembaga_penyiaran SET file_nib = %s WHERE penyiaran_id_origin = %s"
            #     cursor2.execute(sql2, (file_name, idperusahaanfinal_origin, ))
            #     connection2.commit()
            #     print("record updated.", file_name, idperusahaanfinal_origin)
                
            # elif field_name == 'Afiliasi':
            #     # update field file_fotokopi_npwp di tabel lampiran_penyiaran berdasarkan id_perusahaanfinal_origin
            #     sql2 = "UPDATE lembaga_penyiaran SET file_afiliasi = %s WHERE penyiaran_id_origin = %s"
            #     cursor2.execute(sql2, (file_name, idperusahaanfinal_origin, ))
            #     connection2.commit()
            #     print("record updated.", file_name, idperusahaanfinal_origin)

            elif field_name == 'PROYEKSI_PENDAPATAN':
                # update field file_fotokopi_npwp di tabel lampiran_penyiaran berdasarkan id_perusahaanfinal_origin
                sql2 = "UPDATE lampiran_penyiaran SET file_aspek_permodalan = %s WHERE penyiaran_id_origin = %s"
                cursor2.execute(sql2, (file_name, idperusahaanfinal_origin, ))
                connection2.commit()
                print("record updated.", file_name, idperusahaanfinal_origin)

            elif field_name == 'RENCANA_KINERJA_KEUANGAN':
                # update field file_fotokopi_npwp di tabel lampiran_penyiaran berdasarkan id_perusahaanfinal_origin
                sql2 = "UPDATE lampiran_penyiaran SET file_case_flow = %s WHERE penyiaran_id_origin = %s"
                cursor2.execute(sql2, (file_name, idperusahaanfinal_origin, ))
                connection2.commit()
                print("record updated.", file_name, idperusahaanfinal_origin)
                
            else:
                print('tidak ada')

       

def main():
    start_()


if __name__ == "__main__":
    main()
