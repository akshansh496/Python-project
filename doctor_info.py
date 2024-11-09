import sqlite3

conn=sqlite3.connect('hospital.db')
cursor=conn.cursor()

#creation of doctor's table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS DOCTOR_INFO(
               DOCTOR_ID INTEGER PRIMARY KEY AUTOINCREMENT,
               NAME VARCHAR(50) NOT NULL,
               SPECIALISATION VARCHAR(50)    
               )
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
    
doctor_info()

# Commit the transaction
conn.commit()

# Close the connection
conn.close()