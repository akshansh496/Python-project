import sqlite3

conn=sqlite3.connect('hospital.db')
cursor=conn.cursor()

#creation of doctor's table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS DOCTOR_INFO(
               DOCTOR_ID INTEGER PRIMARY KEY AUTOINCREMENT,
               NAME VARCHAR(50) NOT NULL,
               SPECIALISATION VARCHAR(50),
               PASSWORD1 VARCHAR(10)     
               );
''')

#function to add doctor's info
def doctor_info():
    doctor_name=input("Enter your name:").upper()
    specialisation=input("Enter your specialisation if any:").upper()
    cursor.execute('''
        INSERT INTO DOCTOR_INFO
                   (NAME,SPECIALISATION) 
                   VALUES(?,?)      
''',(doctor_name,specialisation))
    doctor_id = cursor.lastrowid
    print(f"Your doctor ID is: {doctor_id}")
    password1=input("CREATE YOUR PASSWORD:").upper()
    cursor.execute('''
    UPDATE DOCTOR_INFO
    SET PASSWORD1=?
    WHERE DOCTOR_ID=?
    ''',(password1,doctor_id))
    conn.commit()
    print("\nYOUR I'D HAS BEEN SUCCESSFULLY CREATED")
doctor_info()

# Close the connection
conn.close()