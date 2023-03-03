import datetime

five_days_ago = datetime.date.today() - datetime.timedelta(days=5)
print("Five Days Ago:", five_days_ago.strftime("%d-%m-%Y"))