import datetime
tday = datetime.date.today ()
bday=datetime.date(2025,6,22)
till_bday=bday-tday
print(till_bday.total_seconds())




def appointment():
    print("AVAILABLE DOCTORS:\n")
    print(f"{'DOCTOR_ID':<12}{'DOCTOR\'S NAME':<20}{'DOCTOR\'S SPECIALISATION':<25}")
    print("-" * 60)  # Print a separator line for better readability

    cursor.execute('''SELECT * FROM DOCTOR_INFO''')
    for row in cursor.fetchall():
        print(f"{row[0]:<12}{row[1]:<20}{row[2]:<25}")

appointment()
