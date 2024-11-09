# import sqlite3
# #create hospital.db
# conn=sqlite3.connect('hospital.db')
# #create a cursor object to interact with the database
# cursor=conn.cursor()
# #create a table of patients
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS PATIENTS(
#             PATIENT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
#             PATIENT_NAME TEXT NOT NULL
#                )
# ''')
# #Function to add a new patient
# def add_patient(patient):
#     cursor.execute('''
#     INSERT INTO PATIENTS(PATIENT_NAME)    
#     VALUES(?)          
#      ''', (patient,))
#     conn.commit()
# add_patient('john doe')
# def display_patients():
#     cursor.execute('SELECT * FROM PATIENTS')
#     patients = cursor.fetchall()
    
#     if patients:
#         for patient in patients:
#             print(f"Patient ID: {patient[0]}, Patient Name: {patient[1]}")
#     else:
#         print("No patients found.")
# display_patientsital.db')

# Create a cursor object to interact with the database


# Close the connection to the database
# conn.close()
# import sqlite3

# # Create hospital.db
# conn = sqlite3.connect('hospital.db')

# # Create a cursor object to interact with the database
# cursor = conn.cursor()

# # Create tables for patients, doctors, and appointments
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS PATIENTS (
#         PATIENT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
#         PATIENT_NAME TEXT NOT NULL
#     )
# ''')

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS DOCTORS (
#         DOCTOR_ID INTEGER PRIMARY KEY AUTOINCREMENT,
#         DOCTOR_NAME TEXT NOT NULL,
#         SPECIALIZATION TEXT NOT NULL
#     )
# ''')

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS APPOINTMENTS (
#         APPOINTMENT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
#         PATIENT_ID INTEGER,
#         DOCTOR_ID INTEGER,
#         APPOINTMENT_DATE TEXT,
#         FOREIGN KEY (PATIENT_ID) REFERENCES PATIENTS (PATIENT_ID),
#         FOREIGN KEY (DOCTOR_ID) REFERENCES DOCTORS (DOCTOR_ID)
#     )
# ''')

# # Function to add a new patient
# def add_patient():
#     patient_name = input("Enter the patient's name: ")
#     cursor.execute('''
#         INSERT INTO PATIENTS (PATIENT_NAME)
#         VALUES (?)
#     ''', (patient_name,))
#     conn.commit()
#     print(f"Patient '{patient_name}' added successfully!")

# # Function to add a new doctor
# def add_doctor():
#     doctor_name = input("Enter the doctor's name: ")
#     specialization = input("Enter the doctor's specialization: ")
#     cursor.execute('''
#         INSERT INTO DOCTORS (DOCTOR_NAME, SPECIALIZATION)
#         VALUES (?, ?)
#     ''', (doctor_name, specialization))
#     conn.commit()
#     print(f"Doctor '{doctor_name}' with specialization '{specialization}' added successfully!")

# # Function to display patients
# def display_patients():
#     cursor.execute('SELECT * FROM PATIENTS')
#     patients = cursor.fetchall()
    
#     if patients:
#         for patient in patients:
#             print(f"Patient ID: {patient[0]}, Patient Name: {patient[1]}")
#     else:
#         print("No patients found.")

# # Function to display doctors
# def display_doctors():
#     cursor.execute('SELECT * FROM DOCTORS')
#     doctors = cursor.fetchall()
    
#     if doctors:
#         for doctor in doctors:
#             print(f"Doctor ID: {doctor[0]}, Doctor Name: {doctor[1]}, Specialization: {doctor[2]}")
#     else:
#         print("No doctors found.")

# # Function to book an appointment
# def book_appointment():
#     display_patients()
#     patient_id = input("Enter the Patient ID for the appointment: ")
    
#     display_doctors()
#     doctor_id = input("Enter the Doctor ID for the appointment: ")
    
#     appointment_date = input("Enter the appointment date (YYYY-MM-DD): ")
    
#     cursor.execute('''
#         INSERT INTO APPOINTMENTS (PATIENT_ID, DOCTOR_ID, APPOINTMENT_DATE)
#         VALUES (?, ?, ?)
#     ''', (patient_id, doctor_id, appointment_date))
#     conn.commit()
#     print("Appointment booked successfully!")

# # Function to display appointments
# def display_appointments():
#     cursor.execute('''
#         SELECT APPOINTMENTS.APPOINTMENT_ID, PATIENTS.PATIENT_NAME, DOCTORS.DOCTOR_NAME, APPOINTMENTS.APPOINTMENT_DATE 
#         FROM APPOINTMENTS
#         JOIN PATIENTS ON APPOINTMENTS.PATIENT_ID = PATIENTS.PATIENT_ID
#         JOIN DOCTORS ON APPOINTMENTS.DOCTOR_ID = DOCTORS.DOCTOR_ID
#     ''')
#     appointments = cursor.fetchall()
    
#     if appointments:
#         for appointment in appointments:
#             print(f"Appointment ID: {appointment[0]}, Patient: {appointment[1]}, Doctor: {appointment[2]}, Date: {appointment[3]}")
#     else:
#         print("No appointments found.")

# # Main loop to add patients, doctors, book appointments, or exit
# while True:
#     choice = input("\nChoose an option: 'patient', 'doctor', 'appointment', 'show appointments', or 'exit': ").strip().lower()
#     if choice == 'patient':
#         add_patient()
#     elif choice == 'doctor':
#         add_doctor()
#     elif choice == 'appointment':
#         book_appointment()
#     elif choice == 'show appointments':
#         display_appointments()
#     elif choice == 'exit':
#         break
#     else:
#         print("Invalid choice. Please try again.")

# # Display final lists of patients, doctors, and appointments
# print("\nFinal Patients list:")
# display_patients()

# print("\nFinal Doctors list:")
# display_doctors()

# print("\nFinal Appointments list:")
# display_appointments()

# # Close the connection to the database
# conn.close()

# import sqlite3

# # Connect to the hospital.db database
# conn = sqlite3.connect('hospital.db')
# cursor = conn.cursor()

# # Create the PATIENTS table if it doesn't exist
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS PATIENTS (
#         PATIENT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
#         PATIENT_NAME TEXT NOT NULL
#     )
# ''')

# # Create the DOCTORS table if it doesn't exist
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS DOCTORS (
#         DOCTOR_ID INTEGER PRIMARY KEY AUTOINCREMENT,
#         DOCTOR_NAME TEXT NOT NULL,
#         SPECIALIZATION TEXT NOT NULL
#     )
# ''')

# # Create the APPOINTMENTS table with APPOINTMENT_TIME column
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS APPOINTMENTS (
#         APPOINTMENT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
#         PATIENT_ID INTEGER,
#         DOCTOR_ID INTEGER,
#         APPOINTMENT_DATE TEXT,
#         APPOINTMENT_TIME TEXT,
#         FOREIGN KEY (PATIENT_ID) REFERENCES PATIENTS (PATIENT_ID),
#         FOREIGN KEY (DOCTOR_ID) REFERENCES DOCTORS (DOCTOR_ID)
#     )
# ''')

# conn.commit()
# print("Tables created successfully.")

# # Function to add a new patient
# def add_patient():
#     patient_name = input("Enter patient name: ")
#     cursor.execute('''
#         INSERT INTO PATIENTS (PATIENT_NAME)
#         VALUES (?)
#     ''', (patient_name,))
#     conn.commit()
#     print(f"Patient '{patient_name}' added successfully.")

# # Function to add a new doctor
# # Function to add a new doctor
# def add_doctor():
#     doctor_name = input("Enter doctor name: ")
#     specialization = input("Enter doctor's specialization: ")  # Prompt for specialization
#     cursor.execute('''
#         INSERT INTO DOCTORS (DOCTOR_NAME, SPECIALIZATION)
#         VALUES (?, ?)
#     ''', (doctor_name, specialization))  # Insert specialization
#     conn.commit()
#     print(f"Doctor '{doctor_name}' with specialization '{specialization}' added successfully.")

# # Function to book an appointment
# def book_appointment():
#     # Display available patients and doctors
#     print("\nAvailable Patients:")
#     cursor.execute("SELECT * FROM PATIENTS")
#     for row in cursor.fetchall():
#         print(f"ID: {row[0]}, Name: {row[1]}")

#     print("\nAvailable Doctors:")
#     cursor.execute("SELECT * FROM DOCTORS")
#     for row in cursor.fetchall():
#         print(f"ID: {row[0]}, Name: {row[1]}")

#     # Collect appointment details from the user
#     patient_id = int(input("Enter Patient ID for the appointment: "))
#     doctor_id = int(input("Enter Doctor ID for the appointment: "))
#     appointment_date = input("Enter appointment date (YYYY-MM-DD): ")
#     appointment_time = input("Enter appointment time (HH:MM): ")

#     cursor.execute('''
#         INSERT INTO APPOINTMENTS (PATIENT_ID, DOCTOR_ID, APPOINTMENT_DATE, APPOINTMENT_TIME)
#         VALUES (?, ?, ?, ?)
#     ''', (patient_id, doctor_id, appointment_date, appointment_time))
#     conn.commit()
#     print("Appointment booked successfully.")

# # Function to display all appointments
# def view_appointments():
#     cursor.execute('''
#         SELECT APPOINTMENTS.APPOINTMENT_ID, PATIENTS.PATIENT_NAME, DOCTORS.DOCTOR_NAME, 
#                APPOINTMENTS.APPOINTMENT_DATE, APPOINTMENTS.APPOINTMENT_TIME
#         FROM APPOINTMENTS
#         JOIN PATIENTS ON APPOINTMENTS.PATIENT_ID = PATIENTS.PATIENT_ID
#         JOIN DOCTORS ON APPOINTMENTS.DOCTOR_ID = DOCTORS.DOCTOR_ID
#     ''')
#     appointments = cursor.fetchall()
#     print("\nAppointments List:")
#     for appointment in appointments:
#         print(f"ID: {appointment[0]}, Patient: {appointment[1]}, Doctor: {appointment[2]}, Date: {appointment[3]}, Time: {appointment[4]}")

# # Main menu
# while True:
#     print("\nHospital Management System")
#     print("1. Add Patient")
#     print("2. Add Doctor")
#     print("3. Book Appointment")
#     print("4. View Appointments")
#     print("5. Exit")
#     choice = input("Enter your choice: ")

#     if choice == '1':
#         add_patient()
#     elif choice == '2':
#         add_doctor()
#     elif choice == '3':
#         book_appointment()
#     elif choice == '4':
#         view_appointments()
#     elif choice == '5':
#         print("Exiting the system.")
#         break
#     else:
#         print("Invalid choice. Please try again.")

# # Close the database connection
# conn.close()

import sqlite3
from datetime import datetime

# Connect to (or create) the hospital database
conn = sqlite3.connect('hospital.db')
cursor = conn.cursor()

# Creation of patient table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS PATIENT_INFO(
        PATIENT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME VARCHAR(50) NOT NULL,
        AGE INTEGER NOT NULL,
        HEIGHT DOUBLE,
        WEIGHT DOUBLE,
        SEX VARCHAR(10) NOT NULL,
        BLOOD_GROUP VARCHAR(10),
        BMI DOUBLE
    );
''')

# Function to add a new patient
def add_patient():
    patient_name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    height = float(input("Enter your height in centimeters: "))
    weight = float(input("Enter your weight in kg: "))
    sex = input("Enter your sex: ")
    blood_group = input("Enter your blood group: ")
    bmi = weight / ((height / 100) ** 2)
    
    cursor.execute('''
        INSERT INTO PATIENT_INFO (NAME, AGE, HEIGHT, WEIGHT, SEX, BLOOD_GROUP, BMI)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (patient_name, age, height, weight, sex, blood_group, bmi))
    
    conn.commit()
    print(f"Patient {patient_name} added successfully with BMI: {bmi:.2f}")
    return cursor.lastrowid

# Creation of doctor table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS DOCTOR_INFO(
        DOCTOR_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME VARCHAR(50) NOT NULL,
        SPECIALISATION VARCHAR(50)
    );
''')

# Function to add doctor's info
def add_doctor():
    doctor_name = input("Enter doctor's name: ")
    specialization = input("Enter doctor's specialization: ")
    
    cursor.execute('''
        INSERT INTO DOCTOR_INFO (NAME, SPECIALISATION)
        VALUES (?, ?)
    ''', (doctor_name, specialization))
    
    conn.commit()
    print(f"Doctor {doctor_name} added successfully.")

# Creation of appointment table
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

# Function to book an appointment
def book_appointment():
    pat_id = int(input("Enter your Patient ID: "))
    
    # Display available doctors
    print("\nAvailable Doctors:")
    print(f"{'DOCTOR_ID':<12}{'NAME':<20}{'SPECIALIZATION':<25}")
    print("-" * 60)
    
    cursor.execute('SELECT * FROM DOCTOR_INFO')
    for row in cursor.fetchall():
        print(f"{row[0]:<12}{row[1]:<20}{row[2]:<25}")
    
    doc_id = int(input("\nEnter the Doctor ID to book an appointment with: "))
    appointment_date = input("Enter the date and time for your appointment (YYYY-MM-DD HH:MM): ")
    appointment_full_date = datetime.strptime(appointment_date, "%Y-%m-%d %H:%M")
    
    cursor.execute('''
        INSERT INTO APPOINTMENT_TABLE (PATIENT_ID, DOCTOR_ID, APPOINTMENT_DATE_TIME)
        VALUES (?, ?, ?)
    ''', (pat_id, doc_id, appointment_full_date))
    
    conn.commit()
    print("Appointment booked successfully.")

# Example usage
# Uncomment to test each function one by one
# add_patient()
# add_doctor()
# book_appointment()

# Close the connection when done
conn.close()