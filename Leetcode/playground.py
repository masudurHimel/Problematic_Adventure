from datetime import datetime

db_time = "2022-06-10T23:57:53.710004+06:00"
formatted_db_time = datetime.strptime(db_time[:-6], "%Y-%m-%dT%H:%M:%S.%f")
current_time = datetime.now()
print("Difference in time : ", current_time - formatted_db_time)
