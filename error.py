import datetime
tday = datetime.date.today ()
bday=datetime.date(2025,6,22)
till_bday=bday-tday
print(till_bday.total_seconds())
