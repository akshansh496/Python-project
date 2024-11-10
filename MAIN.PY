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

    patient_name=input("\nEnter your name:").upper()
    try:
        age=input("\nEnter your age:")
    except:
        print("\nINVALID INPUT")
    try:
        h=float(input("\nEnter your height in centimeter:"))
    except:
        print("\nINAVLID INPUT")
    try:
        w=float(input("\nEnter your weigth in kg:"))
    except:
        print("\nINAVLID INPUT")
    sex=input("\nEnter your sex:").upper()
    bg=input("\nEnter your blood group:").upper()
    bmi=round(w/(h/100)**2,2)
    cursor.execute('''
        INSERT INTO PATIENT_INFO
        (NAME,AGE,HEIGTH,WEIGTH,SEX,BLOOD_GROUP,BMI)
         VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (patient_name, age, h, w, sex, bg, bmi))
    conn.commit()
    #to display patient its patient id
    patient_id = cursor.lastrowid
    print(f"\nYour patient ID is: {patient_id}")
    conn.commit()
    #to store password of each user
    password=input("\nCREATE YOUR PASSWORD:").upper()
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
    doctor_name=input("\nEnter your name:").upper()
    specialisation=input("\nEnter your specialisation if any:").upper()
    cursor.execute('''
        INSERT INTO DOCTOR_INFO
                   (NAME,SPECIALISATION) 
                   VALUES(?,?)      
''',(doctor_name,specialisation))
    doctor_id = cursor.lastrowid
    print(f"\nYour doctor ID is: {doctor_id}")
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
        pat_id=int(input("\nENTER YOUR PATIENT I'D:"))
    except:
        print("\nINAVLID INPUT")
    print("\nAVAILABLE DOCTORS:\n")
    print(f"{'DOCTOR_ID':<12}{'DOCTOR\'S NAME':<20}{'DOCTOR\'S SPECIALISATION':<25}")
    print("-" * 90) 

    cursor.execute('''SELECT * FROM DOCTOR_INFO''')
    for row in cursor.fetchall():
        print(f"{row[0]:<12}{row[1]:<20}{row[2]:<25}")
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
    print(f"\nNew appointment created with ID: {appointment_id}")
    print("\nAPPOINTMENT BOOKED SUCCESSFULLY")
    conn.commit()

#VIEWING MY APPOINTMENTS
def view_appointment():
    pat_id = int(input("\nENTER YOUR PATIENT ID:"))
    
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

#function to login for users already registered
def patient_login():
    id=input("\nENTER YOUR PATIENT ID:")
    passkey=input("\nENTER YOUR PASSWORD:")
    cursor.execute("SELECT * FROM PATIENT_INFO WHERE PATIENT_ID=? AND PASSWORD=?",(id,passkey,))
    rows=cursor.fetchall()
    if rows:
        print(f"{'PATIENT ID':<15}{'NAME':<15}{'AGE':<5}{'HEIGHT':<10}{'WEIGTH':<10}{'SEX':<10}{'BLOOD GROUP':<15}{'BMI':<10}0")
        for row in rows:
            print(f"{row[0]:<15}{row[2]:<15}{row[3]:<5}{row[4]:<10}{row[5]:<10}{row[6]:<10}{row[7]:<15}{row[8]:<10}")
    else:
        print("\nWRONG PATIENT ID OR PASSWORD")
    conn.commit()

#main
print("\nWELCOME TO HOSPITAL MANAGEMENT SYSTEM")
while True:
    print("\n1.CREATE A NEW PROFILE AS PATIENT")
    print("\n2.CREATE A NEW PROFILE AS DOCTOR")     
    print("\n3.LOGIN TO PATIENT ID")
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
        

    
    # print("3.BOOK AN APPOINTMENT")
    # print("4.VIEW MY APPOINTMENTS")
    # print("5. EXIT")
    
    # try:
    #     choice = int(input("Enter your choice: "))
        
    #     if choice == 1:
    #         patient()
    #     elif choice == 2:
    #         doctor_info()
    #     elif choice == 3:
    #         appointment()
    #     elif choice == 4:
    #         view_appointment()
    #     elif choice == 5:
    #         print("Exiting the system.")
    #         break
    #     else:
    #         print("Invalid choice. Please try again.")
    
    # except ValueError:
    #     print("Please enter a valid number.")

conn.commit()

# Close the connection
conn.close()