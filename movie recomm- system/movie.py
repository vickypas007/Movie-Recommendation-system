import csv
import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root',passwd='',database='movie')
print("database connected")

cursor = mydb.cursor()

csv_data = csv.reader(open('mov2.csv'))
for row in csv_data:
    cursor.execute('INSERT INTO movielist(movieid, title,genres,rating )VALUES(%s,%s,%s,%s)', row)
    print(row)


mydb.commit()
cursor.close()
print("Done")