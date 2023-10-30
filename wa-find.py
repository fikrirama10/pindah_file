import openpyxl
import mysql.connector


config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "simp3_user_v2"
}
connection = mysql.connector.connect(**config)

def tes():
    
    wb = openpyxl.load_workbook('wa.xlsx')    
    ws = wb['Sheet1']
    my_list = list()

    for value in ws.iter_rows(
        min_row=2,min_col=3, max_col=4, 
        values_only=True):
        my_list.append(value)
    data = [];   

    for ele1 in my_list:
        data.append(ele1)

    for row in data:
        cursor = connection.cursor(buffered=True)
        cursor.execute("SELECT id,kontak_email,no_wa_korespondensi FROM lembaga_penyiaran WHERE kontak_email = %s", (row[1],))
        result = cursor.fetchone()
        if result:
            id = result[0]
            email = result[1]
            wa = row[0]
            cursor = connection.cursor()
            cursor.execute("UPDATE lembaga_penyiaran SET no_wa_korespondensi = %s WHERE kontak_email = %s", (wa,email,))
            connection.commit()
            print(id,email,wa)
        else:
            print("Tidak ada")

    

tes()