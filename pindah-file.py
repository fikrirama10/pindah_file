import shutil
from mysql.connector import connect, Error
import mysql.connector

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

# absolute path
def pindah_file_latar_belakang():
    connection = destinantion_connection()
    cursor = connection.cursor()
    cursor.execute(" SELECT file_latar_belakang from lampiran_penyiaran  ")
    records = cursor.fetchall()

    for row in records:
        nama_file = row[0]
        # Tentukan path sumber dan path destinasi
        path_sumber = "/var/www/html/app-simp3-pra-migrasi/uploads/lampiran_file_temp/"+str(nama_file)
        path_destinasi = "/home/simp3-rebuild/public/storage/file_latar_belakang/"
        try:
            with open(path_sumber, "r") as file:
                # Lakukan operasi pada file
                shutil.copy(path_sumber, path_destinasi)
                print("berhasil")
        except IsADirectoryError as e:
            print(f"Kesalahan: Ini adalah direktori, bukan file. {e} "+str(nama_file))
        except FileNotFoundError:
            print("Kesalahan: File tidak ditemukan.")
        except PermissionError:
            print("Kesalahan: Izin akses tidak mencukupi.")
        except Exception as e:
            print(f"Kesalahan lain: {e}")

def pindah_maksud_tujuan():
    connection = destinantion_connection()
    cursor = connection.cursor()
    cursor.execute(" SELECT file_maksud_dan_tujuan from lampiran_penyiaran ")
    records = cursor.fetchall()

    for row in records:
        nama_file = row[0]
        # Tentukan path sumber dan path destinasi
        path_sumber = "/var/www/html/app-simp3-pra-migrasi/uploads/lampiran_file_temp/"+str(nama_file)
        path_destinasi = "/home/simp3-rebuild/public/storage/file_maksud_tujuan/"
        try:
            with open(path_sumber, "r") as file:
                # Lakukan operasi pada file
                shutil.copy(path_sumber, path_destinasi)
                print("berhasil")
        except IsADirectoryError as e:
            print(f"Kesalahan: Ini adalah direktori, bukan file. {e} "+str(nama_file))
        except FileNotFoundError:
            print("Kesalahan: File tidak ditemukan.")
        except PermissionError:
            print("Kesalahan: Izin akses tidak mencukupi.")
        except Exception as e:
            print(f"Kesalahan lain: {e}")

def pindah_file_visi_misi():
    connection = destinantion_connection()
    cursor = connection.cursor()
    cursor.execute(" SELECT file_visi_misi from lampiran_penyiaran")
    records = cursor.fetchall()
    for row in records:
        nama_file = row[0]
        # Tentukan path sumber dan path destinasi
        path_sumber = "/var/www/html/app-simp3-pra-migrasi/uploads/lampiran_file_temp/"+str(nama_file)
        path_destinasi = "/home/simp3-rebuild/public/storage/file_visi_misi/"
        try:
            with open(path_sumber, "r") as file:
                # Lakukan operasi pada file
                shutil.copy(path_sumber, path_destinasi)
                print("berhasil")
        except IsADirectoryError as e:
            print(f"Kesalahan: Ini adalah direktori, bukan file. {e} "+str(nama_file))
        except FileNotFoundError:
            print("Kesalahan: File tidak ditemukan.")
        except PermissionError:
            print("Kesalahan: Izin akses tidak mencukupi.")
        except Exception as e:
            print(f"Kesalahan lain: {e}")

def pindah_file_data_keuangan():
    connection = destinantion_connection()
    cursor = connection.cursor()
    cursor.execute(" SELECT file_data_keuangan from lampiran_penyiaran  ")
    records = cursor.fetchall()
    for row in records:
        nama_file = row[0]
        # Tentukan path sumber dan path destinasi
        path_sumber = "/var/www/html/app-simp3-pra-migrasi/uploads/lampiran_file_temp/"+str(nama_file)
        path_destinasi = "/home/simp3-rebuild/public/storage/file_data_keuangan/"
        try:
            with open(path_sumber, "r") as file:
                # Lakukan operasi pada file
                shutil.copy(path_sumber, path_destinasi)
                print("berhasil")
        except IsADirectoryError as e:
            print(f"Kesalahan: Ini adalah direktori, bukan file. {e} "+str(nama_file))
        except FileNotFoundError:
            print("Kesalahan: File tidak ditemukan.")
        except PermissionError:
            print("Kesalahan: Izin akses tidak mencukupi.")
        except Exception as e:
            print(f"Kesalahan lain: {e}")

def pindah_file_scan_ipp():
    connection = destinantion_connection()
    cursor = connection.cursor()
    cursor.execute(" SELECT file_scan_ipp from lampiran_penyiaran  ")
    records = cursor.fetchall()
    for row in records:
        nama_file = row[0]
        # Tentukan path sumber dan path destinasi
        path_sumber = "/var/www/html/app-simp3-pra-migrasi/uploads/lampiran_file_temp/"+str(nama_file)
        path_destinasi = "/home/simp3-rebuild/public/storage/file_scan_ipp/"
        try:
            with open(path_sumber, "r") as file:
                # Lakukan operasi pada file
                shutil.copy(path_sumber, path_destinasi)
                print("berhasil")
        except IsADirectoryError as e:
            print(f"Kesalahan: Ini adalah direktori, bukan file. {e} "+str(nama_file))
        except FileNotFoundError:
            print("Kesalahan: File tidak ditemukan.")
        except PermissionError:
            print("Kesalahan: Izin akses tidak mencukupi.")
        except Exception as e:
            print(f"Kesalahan lain: {e}")


def pindah_file_akta_pendirian():
    connection = destinantion_connection()
    cursor = connection.cursor()
    cursor.execute(" SELECT file_akta_pendirian from lampiran_penyiaran")
    records = cursor.fetchall()
    for row in records:
        nama_file = row[0]
        # Tentukan path sumber dan path destinasi
        path_sumber = "/var/www/html/app-simp3-pra-migrasi/uploads/lampiran_file_temp/"+str(nama_file)
        path_destinasi = "/home/simp3-rebuild/public/storage/file_akta_pendirian/"
        try:
            with open(path_sumber, "r") as file:
                # Lakukan operasi pada file
                shutil.copy(path_sumber, path_destinasi)
                print("berhasil")
        except IsADirectoryError as e:
            print(f"Kesalahan: Ini adalah direktori, bukan file. {e} "+str(nama_file))
        except FileNotFoundError:
            print("Kesalahan: File tidak ditemukan.")
        except PermissionError:
            print("Kesalahan: Izin akses tidak mencukupi.")
        except Exception as e:
            print(f"Kesalahan lain: {e}")

def pindah_file_akta_perubahan():
    connection = destinantion_connection()
    cursor = connection.cursor()
    cursor.execute(" SELECT file_akta_perubahan from lampiran_penyiaran ")
    records = cursor.fetchall()
    for row in records:
        nama_file = row[0]
        # Tentukan path sumber dan path destinasi
        path_sumber = "/var/www/html/app-simp3-pra-migrasi/uploads/lampiran_file_temp/"+str(nama_file)
        path_destinasi = "/home/simp3-rebuild/public/storage/file_akta_perubahan/"
        try:
            with open(path_sumber, "r") as file:
                # Lakukan operasi pada file
                shutil.copy(path_sumber, path_destinasi)
                print("berhasil")
        except IsADirectoryError as e:
            print(f"Kesalahan: Ini adalah direktori, bukan file. {e} "+str(nama_file))
        except FileNotFoundError:
            print("Kesalahan: File tidak ditemukan.")
        except PermissionError:
            print("Kesalahan: Izin akses tidak mencukupi.")
        except Exception as e:
            print(f"Kesalahan lain: {e}")

def pindah_file_surat_pernyataan():
    connection = destinantion_connection()
    cursor = connection.cursor()
    cursor.execute(" SELECT file_surat_pernyataan from lampiran_penyiaran ")
    records = cursor.fetchall()
    for row in records:
        nama_file = row[0]
        # Tentukan path sumber dan path destinasi
        path_sumber = "/var/www/html/app-simp3-pra-migrasi/uploads/lampiran_file_temp/"+str(nama_file)
        path_destinasi = "/home/simp3-rebuild/public/storage/file_surat_pernyataan/"
        try:
            with open(path_sumber, "r") as file:
                # Lakukan operasi pada file
                shutil.copy(path_sumber, path_destinasi)
                print("berhasil")
        except IsADirectoryError as e:
            print(f"Kesalahan: Ini adalah direktori, bukan file. {e} "+str(nama_file))
        except FileNotFoundError:
            print("Kesalahan: File tidak ditemukan.")
        except PermissionError:
            print("Kesalahan: Izin akses tidak mencukupi.")
        except Exception as e:
            print(f"Kesalahan lain: {e}")

def pindah_file_scan_isr():
    connection = destinantion_connection()
    cursor = connection.cursor()
    cursor.execute(" SELECT file_scan_isr from lampiran_penyiaran ")
    records = cursor.fetchall()
    for row in records:
        nama_file = row[0]
        # Tentukan path sumber dan path destinasi
        path_sumber = "/var/www/html/app-simp3-pra-migrasi/uploads/lampiran_file_temp/"+str(nama_file)
        path_destinasi = "/home/simp3-rebuild/public/storage/file_isr/"
        try:
            with open(path_sumber, "r") as file:
                # Lakukan operasi pada file
                shutil.copy(path_sumber, path_destinasi)
                print("berhasil")
        except IsADirectoryError as e:
            print(f"Kesalahan: Ini adalah direktori, bukan file. {e} "+str(nama_file))
        except FileNotFoundError:
            print("Kesalahan: File tidak ditemukan.")
        except PermissionError:
            print("Kesalahan: Izin akses tidak mencukupi.")
        except Exception as e:
            print(f"Kesalahan lain: {e}")

def pindah_file_data_keuangan():
    connection = destinantion_connection()
    cursor = connection.cursor()
    cursor.execute(" SELECT file_data_keuangan from lampiran_penyiaran ")
    records = cursor.fetchall()
    for row in records:
        nama_file = row[0]
        # Tentukan path sumber dan path destinasi
        path_sumber = "/var/www/html/app-simp3-pra-migrasi/uploads/lampiran_file_temp/"+str(nama_file)
        path_destinasi = "/home/simp3-rebuild/public/storage/file_data_keuangan/"
        try:
            with open(path_sumber, "r") as file:
                # Lakukan operasi pada file
                shutil.copy(path_sumber, path_destinasi)
                print("berhasil")
        except IsADirectoryError as e:
            print(f"Kesalahan: Ini adalah direktori, bukan file. {e} "+str(nama_file))
        except FileNotFoundError:
            print("Kesalahan: File tidak ditemukan.")
        except PermissionError:
            print("Kesalahan: Izin akses tidak mencukupi.")
        except Exception as e:
            print(f"Kesalahan lain: {e}")

def pindah_file_aspek_managemen():
    connection = destinantion_connection()
    cursor = connection.cursor()
    cursor.execute(" SELECT file_aspek_managemen from lampiran_penyiaran ")
    records = cursor.fetchall()
    for row in records:
        nama_file = row[0]
        # Tentukan path sumber dan path destinasi
        path_sumber = "/var/www/html/app-simp3-pra-migrasi/uploads/lampiran_file_temp/"+str(nama_file)
        path_destinasi = "/home/simp3-rebuild/public/storage/file_aspek_managemen/"
        try:
            with open(path_sumber, "r") as file:
                # Lakukan operasi pada file
                shutil.copy(path_sumber, path_destinasi)
                print("berhasil")
        except IsADirectoryError as e:
            print(f"Kesalahan: Ini adalah direktori, bukan file. {e} "+str(nama_file))
        except FileNotFoundError:
            print("Kesalahan: File tidak ditemukan.")
        except PermissionError:
            print("Kesalahan: Izin akses tidak mencukupi.")
        except Exception as e:
            print(f"Kesalahan lain: {e}")

def pindah_file_pks_mux():
    connection = destinantion_connection()
    cursor = connection.cursor()
    cursor.execute(" SELECT file_pks_mux from lampiran_penyiaran WHERE file_pks_mux IS NOT NULL ")
    records = cursor.fetchall()
    for row in records:
        nama_file = row[0]
        # print(nama_file)
        # Tentukan path sumber dan path destinasi
        path_sumber = "/var/www/html/app-simp3-pra-migrasi/uploads/lampiran_file_temp/"+str(nama_file)
        path_destinasi = "/home/simp3-rebuild/public/storage/file_pks_mux/"
        try:
            with open(path_sumber, "r") as file:
                # Lakukan operasi pada file
                shutil.copy(path_sumber, path_destinasi)
                print("berhasil")
        except IsADirectoryError as e:
            print(f"Kesalahan: Ini adalah direktori, bukan file. {e} "+str(nama_file))
        except FileNotFoundError:
            print("Kesalahan: File tidak ditemukan.")
        except PermissionError:
            print("Kesalahan: Izin akses tidak mencukupi.")
        except Exception as e:
            print(f"Kesalahan lain: {e}")

def pindah_file_nib():
    connection = destinantion_connection()
    cursor = connection.cursor()
    cursor.execute(" SELECT file_nib from lembaga_penyiaran WHERE file_nib IS NOT NULL ")
    records = cursor.fetchall()
    for row in records:
        nama_file = row[0]
        # print(nama_file)
        # Tentukan path sumber dan path destinasi
        path_sumber = "/var/www/html/app-simp3-pra-migrasi/uploads/lampiran_file_temp/"+str(nama_file)
        path_destinasi = "/home/simp3-rebuild/public/storage/file_nib/"
        try:
            with open(path_sumber, "r") as file:
                # Lakukan operasi pada file
                shutil.copy(path_sumber, path_destinasi)
                print("berhasil")
        except IsADirectoryError as e:
            print(f"Kesalahan: Ini adalah direktori, bukan file. {e} "+str(nama_file))
        except FileNotFoundError:
            print("Kesalahan: File tidak ditemukan.")
        except PermissionError:
            print("Kesalahan: Izin akses tidak mencukupi.")
        except Exception as e:
            print(f"Kesalahan lain: {e}")

def pindah_file_rencana_konfigurasi():
    connection = destinantion_connection()
    cursor = connection.cursor()
    cursor.execute(" SELECT file_rencana_konfigurasi from lampiran_penyiaran WHERE file_rencana_konfigurasi IS NOT NULL ")
    records = cursor.fetchall()
    for row in records:
        nama_file = row[0]
        # print(nama_file)
        # Tentukan path sumber dan path destinasi
        path_sumber = "/var/www/html/app-simp3-pra-migrasi/uploads/lampiran_file_temp/"+str(nama_file)
        path_destinasi = "/home/simp3-rebuild/public/storage/file_rencana_konfigurasi_jaringan/"
        try:
            with open(path_sumber, "r") as file:
                # Lakukan operasi pada file
                shutil.copy(path_sumber, path_destinasi)
                print("berhasil")
        except IsADirectoryError as e:
            print(f"Kesalahan: Ini adalah direktori, bukan file. {e} "+str(nama_file))
        except FileNotFoundError:
            print("Kesalahan: File tidak ditemukan.")
        except PermissionError:
            print("Kesalahan: Izin akses tidak mencukupi.")
        except Exception as e:
            print(f"Kesalahan lain: {e}")

def pindah():
    # using input() to take user input
    print("Pilih Nomor Untuk Pindah File :")
    print("1. Pindah File Latar Belakang")
    print("2. Pindah File Maksud dan Tujuan")
    print("3. Pindah File Visi dan Misi")
    print("4. Pindah File Data Keuangan")
    print("5. Pindah File Scan IPP")
    print("6. Pindah File Lampiran Akta Pendirian")
    print("7. Pindah File Lampiran Akta Perubahan")
    print("8. Pindah File Lampiran Surat Pernyataan")
    print("9. Pindah File Scan ISR")
    print("10. Pindah File Rencana Kinerja Keuangan")
    print("11. Pindah File Aspek Managemen")
    print("12. Pindah File PKS MUX")
    print("13. Pindah File Lampiran NIB")
    print("14. Pindah File Konfigurasi Jaringan")


    num = input('Masukan Nomor: ')
    match num:
        case '1':
            print("Pindah File Latar Belakang")
            pindah_file_latar_belakang()
        case '2':
            print("Pindah File Maksud dan Tujuan")
            pindah_maksud_tujuan()
        case '3':
            print("Pindah File Visi dan Misi")
            pindah_file_visi_misi()
        case '4':
            print("Pindah File Data Keuangan")
            pindah_file_data_keuangan()
        case '5':
            print("Pindah File Scan IPP")
            pindah_file_scan_ipp()
        case '6':
            print("Pindah File Lampiran Akta Pendirian")
            pindah_file_akta_pendirian()
        case '7':
            print("Pindah File Lampiran Akta Perubahan")
            pindah_file_akta_perubahan()
        case '8':
            print("Pindah File Lampiran Surat Pernyataan")
            pindah_file_surat_pernyataan()
        case '9':
            print("Pindah File Scan ISR")
            pindah_file_scan_isr()
        case '10':
            print("Pindah File Lampiran Data Keuangan")
            pindah_file_data_keuangan()
        case '11':
            print("Pindah File Aspek Managemen")
            pindah_file_aspek_managemen()
        case '12':
            print("Pindah File PKS MUX")
            pindah_file_pks_mux()
        case '13':
            print("Pindah File NIB")
            pindah_file_nib()
        case '14':
            print("Pindah File Konfigurasi Jaringan")
            pindah_file_nib()
        case _:
            print('Invalid input')

        
    print('You Entered:', num)

    print('Data type of num:', type(num))

    pindah()
    
pindah()