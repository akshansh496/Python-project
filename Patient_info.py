import sqlite3

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
    patient_name=input("Enter your name:").upper()
    age=input("Enter your age:")
    h=float(input("Enter your height in centimeter:"))
    w=float(input("Enter your weigth in kg:"))
    sex=input("Enter your sex:").upper()
    bg=input("Enter your blood group:").upper()
    bmi=round(w/(h/100)**2,2)
    cursor.execute('''
        INSERT INTO PATIENT_INFO
        (NAME,AGE,HEIGTH,WEIGTH,SEX,BLOOD_GROUP,BMI)
         VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (patient_name, age, h, w, sex, bg, bmi))


    #to display patient its patient id
    patient_id = cursor.lastrowid
    print(f"Your patient ID is: {patient_id}")

    #to store password of each user
    password=input("CREATE YOUR PASSWORD").upper()
    cursor.execute('''
    UPDATE PATIENT_INFO
    SET PASSWORD=?
    WHERE PATIENT_ID=?
    ''',(password,patient_id))
patient()


conn.commit()

# Close the connection
conn.close()

# import sqlite3

# conn = sqlite3.connect('hospital.db')
# cursor = conn.cursor()

# # Drop table if it already exists to apply the updated schema
# cursor.execute("DROP TABLE IF EXISTS PATIENT_INFO")

# # Creation of patient's table
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS PATIENT_INFO(
#         PATIENT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
#         PASSWORD VARCHAR(10),
#         NAME VARCHAR(50) NOT NULL,
#         AGE INTEGER NOT NULL,
#         HEIGTH DOUBLE,
#         WEIGTH DOUBLE,
#         SEX VARCHAR(10) NOT NULL,
#         BLOOD_GROUP VARCHAR(10),
#         BMI DOUBLE
#     );
# ''')

# # Function to add a new patient
# def patient():
#     patient_name = input("Enter your name: ")
#     age = input("Enter your age: ")
#     h = float(input("Enter your height in centimeters: "))
#     w = float(input("Enter your weight in kg: "))
#     sex = input("Enter your sex: ")
#     bg = input("Enter your blood group: ")
#     bmi = w / (h / 100) ** 2

#     cursor.execute('''
#         INSERT INTO PATIENT_INFO
#         (NAME, AGE, HEIGTH, WEIGTH, SEX, BLOOD_GROUP, BMI)
#         VALUES (?, ?, ?, ?, ?, ?, ?)
#     ''', (patient_name, age, h, w, sex, bg, bmi))
#     conn.commit()

#     # Get the last inserted patient ID
#     patient_id = cursor.lastrowid
#     print(f"Your patient ID is: {patient_id}")

#     # Prompt to create a password and update the patient's password
#     password = input("Create your password: ")
#     cursor.execute('''
#         UPDATE PATIENT_INFO
#         SET PASSWORD = ?
#         WHERE PATIENT_ID = ?
#     ''', (password, patient_id))
#     conn.commit()

#     print("Password added successfully!")

# # Add a new patient
# patient() 

# # Close the connection
# conn.close()