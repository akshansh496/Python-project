import sqlite3
from datetime import datetime

conn=sqlite3.connect('hospital.db')
cursor=conn.cursor()

#function to login for users already registered
def patient_login():
    id=input("ENTER YOUR PATIENT ID:")
    passkey=input("ENTER YOUR PASSWORD:")
    cursor.execute("SELECT * FROM PATIENT_INFO WHERE PATIENT_ID=? AND PASSWORD=?",(id,passkey,))
    rows=cursor.fetchall()
    if rows:
        print(f"{'PATIENT ID':<15}{'NAME':<15}{'AGE':<5}{'HEIGHT':<10}{'WEIGTH':<10}{'SEX':<10}{'BLOOD GROUP':<15}{'BMI':<10}0")
        for row in rows:
            print(f"{row[0]:<15}{row[2]:<15}{row[3]:<5}{row[4]:<10}{row[5]:<10}{row[6]:<10}{row[7]:<15}{row[8]:<10}")
    else:
        print("WRONG PATIENT ID OR PASSWORD")
patient_login()