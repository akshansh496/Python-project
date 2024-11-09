import sqlite3
from datetime import datetime

conn=sqlite3.connect('hospital.db')
cursor=conn.cursor()

#Creation of appointment table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS APPOINTMENT_TABLE(
               APPOINTMENT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
               PATIENT_ID INTEGER NOT NULL,
               DOCTOR_ID INTEGER NOT NULL,
               APPOINTMENT_DATE_TIME VARCHAR(50) NOT NULL,
               FOREIGN KEY (PATIENT_ID) REFERENCES PATIENT_INFO (PATIENT_ID),
               FOREIGN KEY (DOCTOR_ID) REFERENCES DOCTOR_INFO (DOCTOR_ID)
               );
''')

#function to book appointment
def appointment():
    try:
        pat_id=int(input("ENTER YOUR PATIENT I'D:"))
    except:
        print("INAVLID INPUT")
    print("AVAILABLE DOCTORS:\n")
    print(f"{'DOCTOR_ID':<12}{'DOCTOR\'S NAME':<20}{'DOCTOR\'S SPECIALISATION':<25}")
    print("-" * 90) 

    cursor.execute('''SELECT * FROM DOCTOR_INFO''')
    for row in cursor.fetchall():
        print(f"{row[0]:<12}{row[1]:<20}{row[2]:<25}")
    try:
        doc_id=int(input("ENTER DOCTOR ID WITH WHOM YOU WANT TO BOOK APPOINTMENT:"))
    except:
        print("INVALID INPUT")
    while True:
        try:
            appointment_date = input("ENTER DATE AND TIME FOR YOUR APPOINTMENT (YYYY-MM-DD HH-MM): ")
            appointment_full_date = datetime.strptime(appointment_date, "%Y-%m-%d %H:%M")
            
            # Check if the entered date and time are in the future
            if appointment_full_date < datetime.now():
                print("ERROR: Appointment date and time must be in the future. Please try again.")
            else:
                break
        except ValueError:
            print("INVALID DATE FORMAT. Please use YYYY-MM-DD HH-MM format.")

    cursor.execute('''
    INSERT INTO APPOINTMENT_TABLE
                   (PATIENT_ID,DOCTOR_ID,APPOINTMENT_DATE_TIME)
                   VALUES(?,?,?)
''',(pat_id,doc_id,str(appointment_full_date)))
    appointment_id = cursor.lastrowid
    print(f"New appointment created with ID: {appointment_id}")
    print("APPOINTMENT BOOKED SUCCESSFULLY")
    conn.commit()
appointment()
# Close the connection
conn.close()