import sqlite3
from datetime import datetime

conn=sqlite3.connect('hospital.db')
cursor=conn.cursor()

#Creation of patient's table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS PATIENT_INFO(
        PATIENT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        PASSWORD VARCHAR(10) NOT NULL,
        NAME VARCHAR(50) NOT NULL,
        AGE INTEGER NOT NULL,
        HEIGTH DOUBLE ,
        WEIGTH DOUBLE ,
        SEX VARCHAR(10) NOT NULL,
        BLOOD_GROUP VARCHAR(10),
        BMI DOUBLE
        );
''')

#function to add a new patient
def patient():

    patient_name=input("Enter your name:")
    try:
        age=input("Enter your age:")
    except:
        print("INVALID INPUT")
    try:
        h=float(input("Enter your height in centimeter:"))
    except:
        print("INAVLID INPUT")
    try:
        w=float(input("Enter your weigth in kg:"))
    except:
        print("INAVLID INPUT")
    sex=input("Enter your sex:")
    bg=input("Enter your blood group:")
    bmi=w/(h/100)**2
    cursor.execute('''
        INSERT INTO PATIENT_INFO
        (NAME,AGE,HEIGTH,WEIGTH,SEX,BLOOD_GROUP,BMI)
         VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (patient_name, age, h, w, sex, bg, bmi))
    conn.commit()
    #to display patient its patient id
    patient_id = cursor.lastrowid
    print(f"Your patient ID is: {patient_id}")
    conn.commit()
    #to store password of each user
    password=input("CREATE YOUR PASSWORD:")
    cursor.execute('''
    UPDATE PATIENT_INFO
    SET PASSWORD=?
    WHERE PATIENT_ID=?
    ''',(password,patient_id))
    conn.commit()
    print("\nYOUR I'D HAS BEEN SUCCESSFULLY CREATED")


#creation of doctor's table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS DOCTOR_INFO(
               DOCTOR_ID INTEGER PRIMARY KEY AUTOINCREMENT,
               NAME VARCHAR(50) NOT NULL,
               SPECIALISATION VARCHAR(50)    
               );
''')

#function to add doctor's info
def doctor_info():
    doctor_name=input("Enter your name:")
    specialisation=input("Enter your specialisation if any:")
    cursor.execute('''
        INSERT INTO DOCTOR_INFO
                   (NAME,SPECIALISATION) 
                   VALUES(?,?)      
''',(doctor_name,specialisation))
    doctor_id = cursor.lastrowid
    print(f"Your doctor ID is: {doctor_id}")
    conn.commit()

#Creation of appointment table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS APPOINTMENT_TABLE(
               APPOINTMENT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
               PATIENT_ID INTEGER NOT NULL,
               DOCTOR_ID INTEGER NOT NULL,
               APPOINTMENT_DATE_TIME VARCHAR(20) NOT NULL,
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
    print("APPOINTMENT BOOKED SUCCESSFULLY")
    conn.commit()

#VIEWING MY APPOINTMENTS
def view_appointment():
    pat_id=int(input("ENTER YOUR PATIENT ID:"))
    cursor.execute("SELECT PATIENT_ID FROM APPOINTMENT_TABLE WHERE PATIENT_ID=?",(pat_id,))
    patient_ids = cursor.fetchall()
    if patient_ids:
            print(f"{'PATIENT_ID':<12}{'DOCTOR_ID':<12}{'APPOINTMENT_ID':<20}{'DATE AND TIME':<30}")
            print("-"*60)
            cursor.execute('SELECT * FROM APPOINTMENT_TABLE WHERE PATIENT_ID=?',(pat_id,))
            rows= cursor.fetchall()
            for row in rows:
                print(f"{row[0]:<12}{row[1]:<12}{row[2]:<20}{row[3]:<30}")
    else:
            print("YOU DON'T HAVE ANY APPOINTMENT")

    conn.commit()

#main
print("\nWELCOME TO HOSPITAL MANAGEMENT SYSTEM")
while True:
    print("\n1.CREATE A NEW PROFILE AS PATIENT")
    print("2.CREATE A NEW PROFILE AS DOCTOR")     
    print("3.BOOK AN APPOINTMENT")
    print("4.VIEW MY APPOINTMENTS")
    print("5. EXIT")
    
    try:
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            patient()
        elif choice == 2:
            doctor_info()
        elif choice == 3:
            appointment()
        elif choice == 4:
            view_appointment()
        elif choice == 5:
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")
    
    except ValueError:
        print("Please enter a valid number.")

conn.commit()

# Close the connection
conn.close()
