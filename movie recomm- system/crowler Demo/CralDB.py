import csv
import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root',passwd='',database='crawler')
print("database connected")

cursor = mydb.cursor()

csv_data = csv.reader(open('output1.csv'))
for row in csv_data:
    cursor.execute('INSERT INTO movielist(title,actor,year )VALUES(%s,%s,%s)', row)
    print(row)


mydb.commit()
cursor.close()
print("Done")