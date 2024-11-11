import sqlite3
from datetime import datetime

conn=sqlite3.connect('hospital.db')
cursor=conn.cursor()

#Creation of patient's table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS PATIENT_INFO(
        PATIENT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        PASSWORD VARCHAR(10),
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

    patient_name=input("\nEnter your name:").upper()
    try:
        age=input("\nEnter your age:")
    except:
        print("\nINVALID INPUT")
    try:
        h=input("\nEnter your height in centimeter:")
    except:
        print("\nINAVLID INPUT")
    try:
        w=input("\nEnter your weigth in kg:")
    except:
        print("\nINAVLID INPUT")
    sex=input("\nEnter your sex:").upper()
    bg=input("\nEnter your blood group:").upper()
    bmi=round(float(w)/(float(h)/100)**2,2)
    password=input("\nCREATE YOUR PASSWORD:").upper()
    cursor.execute('''
        INSERT INTO PATIENT_INFO
        (NAME,AGE,HEIGTH,WEIGTH,SEX,BLOOD_GROUP,BMI,PASSWORD)
         VALUES (?, ?, ?, ?, ?, ?, ?,?)
    ''', (patient_name, age, h, w, sex, bg, bmi,password))
    conn.commit()
    #to display patient its patient id
    patient_id = cursor.lastrowid
    print(f"\nYour patient ID is: {patient_id}")
    conn.commit()
    print("\nYOUR I'D HAS BEEN SUCCESSFULLY CREATED")

#creation of doctor's table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS DOCTOR_INFO(
               DOCTOR_ID INTEGER PRIMARY KEY AUTOINCREMENT,
               NAME VARCHAR(50) NOT NULL,
               SPECIALISATION VARCHAR(50),
               PASSWORD1 VARCHAR(10) NOT NULL     
               );
''')

#function to add doctor's info
def doctor_info():
    doctor_name=input("\nENTER YOUR NAME:").upper()
    specialisation=input("\nENTER YOUR SPECIALISATION IF ANY:").upper()
    password1=input("\nCREATE YOUR PASSWORD:").upper()
    cursor.execute('''
        INSERT INTO DOCTOR_INFO
                   (NAME,SPECIALISATION,PASSWORD1) 
                   VALUES(?,?,?)      
''',(doctor_name,specialisation,password1))
    doctor_id = cursor.lastrowid
    print(f"Your doctor ID is: {doctor_id}")
    conn.commit()
    print("\nYOUR I'D HAS BEEN SUCCESSFULLY CREATED")

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

def appointment(a):
    try:
        pat_id=a
    except:
        print("\nINAVLID INPUT")
    print("\nAVAILABLE DOCTORS:\n")
    print(f"{'DOCTOR_ID':<12}{'DOCTOR\'S NAME':<30}{'DOCTOR\'S SPECIALISATION':<25}")
    print("-" * 90) 

    cursor.execute('''SELECT * FROM DOCTOR_INFO''')
    for row in cursor.fetchall():
        print(f"{row[0]:<12}{row[1]:<30}{row[2]:<25}")
    try:
        doc_id=int(input("\nENTER DOCTOR ID WITH WHOM YOU WANT TO BOOK APPOINTMENT:"))
    except:
        print("\nINVALID INPUT")
    while True:
        try:
            appointment_date = input("\nENTER DATE AND TIME FOR YOUR APPOINTMENT (YYYY-MM-DD HH-MM): ")
            appointment_full_date = datetime.strptime(appointment_date, "%Y-%m-%d %H:%M")
            
            # Check if the entered date and time are in the future
            if appointment_full_date < datetime.now():
                print("\nERROR: Appointment date and time must be in the future. Please try again.")
            cursor.execute('''
                SELECT * FROM APPOINTMENT_TABLE 
                WHERE DOCTOR_ID = ? AND APPOINTMENT_DATE_TIME = ?
            ''', (doc_id, str(appointment_full_date)))
            
            if cursor.fetchone():
                print("\nERROR: This doctor already has an appointment at the specified date and time. Please choose a different time.")
            else:
                break
        except ValueError:
            print("\nINVALID DATE FORMAT. Please use YYYY-MM-DD HH-MM format.")

    cursor.execute('''
    INSERT INTO APPOINTMENT_TABLE
                   (PATIENT_ID,DOCTOR_ID,APPOINTMENT_DATE_TIME)
                   VALUES(?,?,?)
''',(pat_id,doc_id,str(appointment_full_date)))
    appointment_id = cursor.lastrowid
    print(f"\nYour appointment ID: {appointment_id}")
    print("\nAPPOINTMENT BOOKED SUCCESSFULLY")
    conn.commit()

#VIEWING MY APPOINTMENTS
def view_appointment(d):
    pat_id =d
    
    # Fetch appointments for the given PATIENT_ID
    cursor.execute("SELECT * FROM APPOINTMENT_TABLE WHERE PATIENT_ID=?", (pat_id,))
    rows = cursor.fetchall()
    if rows:
        print(f"{'APPOINTMENT_ID':<20}{'PATIENT_ID':<12}{'DOCTOR_ID':<12}{'DATE AND TIME':<30}")
        print("-" * 60)
        for row in rows:   
            print(f"{row[0]:<20}{row[1]:<12}{row[2]:<12}{row[3]:<30}")
    else:
        print("\nYOU DON'T HAVE ANY APPOINTMENTS")

    conn.commit()

def view_doctor_appointment(d):
    doc_id =d
        # Fetch appointments for the given DOCTOR_ID
    cursor.execute("SELECT * FROM APPOINTMENT_TABLE WHERE DOCTOR_ID=?",(doc_id,))
    rows = cursor.fetchall()
    if rows:
        print(f"\n{'APPOINTMENT_ID':<20}{'PATIENT_ID':<12}{'DOCTOR_ID':<12}{'DATE AND TIME':<30}")
        print("-" * 60)
        for row in rows:   
            print(f"{row[0]:<20}{row[1]:<12}{row[2]:<12}{row[3]:<30}")
    else:
        print("YOU DON'T HAVE ANY APPOINTMENTS")

    conn.commit()

#function to login for users already registered
def patient_login():
    id=input("\nENTER YOUR PATIENT ID:")
    passkey=input("\nENTER YOUR PASSWORD:")
    cursor.execute("SELECT * FROM PATIENT_INFO WHERE PATIENT_ID=? AND PASSWORD=?",(id,passkey,))
    rows=cursor.fetchall()
    if rows:
        print(f"{'PATIENT ID':<15}{'NAME':<30}{'AGE':<5}{'HEIGHT':<10}{'WEIGTH':<10}{'SEX':<10}{'BLOOD GROUP':<15}{'BMI':<10}")
        print("_"*100)
        for row in rows:
            print(f"{row[0]:<15}{row[2]:<30}{row[3]:<5}{row[4]:<10}{row[5]:<10}{row[6]:<10}{row[7]:<15}{row[8]:<10}")

        while True:
            print("\n1.BOOK AN APPOINTMENT")
            print("\n2.VIEW MY APPOINTMENTS")
            print("\n3. EXIT")
            try:
                choice2=int(input("ENTER YOUR CHOICE:"))
                if choice2==1:
                    appointment(id)
                elif choice2==2:
                    view_appointment(id)
                elif choice2==3:
                    print("Exiting the patient portal")
                    break
                else:
                    print("INVALID INPUT")
            except:
                print("INVALID INPUT")
    else:
        print("\nWRONG PATIENT ID OR PASSWORD")
    conn.commit()
    
#function to login to existing doctor id
def doctor_login():
    d_id=input("\nENTER YOUR ID:")
    passkey1=input("\nENTER YOUR PASSWORD:")
    cursor.execute('''SELECT * FROM DOCTOR_INFO WHERE DOCTOR_ID=? AND PASSWORD1=?''',(d_id,passkey1))
    rows=cursor.fetchall()
    if rows:
        print(f"\n{'DOCTOR_ID':<15}{'DOCTOR NAME':<30}{'SPECIALISATION':<50}")
        print("-"*100)
        for row in rows:
            print(f"{row[0]:<15}{row[1]:<30}{row[2]:<50}")
    else:
        print("\nWRONG DOCTOR ID OR PASSWORD")
    while True:
        print("\n1.VIEW APPOINTMENTS")
        print("\n2.EXIT")
        try:
            choice2=int(input("\nENTER YOUR CHOICE:"))
            match choice2:
                case 1:
                    view_doctor_appointment(d_id)
                case 2:
                    print("\nEXITING THE DOCTOR PORTAL")
                    break
        except:
            print("\nINVALID INPUT")

#main
print("\nWELCOME TO HOSPITAL MANAGEMENT SYSTEM")
while True:
    print("\n1.CREATE A NEW PROFILE AS PATIENT")
    print("\n2.CREATE A NEW PROFILE AS DOCTOR")     
    print("\n3.LOGIN TO PATIENT ID")
    print("\n4.LOGIN TO DOCTOR ID")
    print("\n5.. EXIT")
    try:
        choice1=int(input("\nENTER YOUR CHOICE:"))
    except ValueError:
        print("\nPlease enter a valid number.")
    match choice1:
        case 1:
            patient()
        case 2:
            doctor_info()
        case 3:
            patient_login()
        case 4:
            doctor_login()
        case 5:
            print("EXITING THE SYSTEM.")
            break
        case _:
            print("INVALID INPUT")
        
conn.commit()

# Close the connection
conn.close()q
