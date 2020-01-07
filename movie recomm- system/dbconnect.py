import csv
import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root',passwd='',database='book')
print("database connected")
cursor = mydb.cursor()

csv_data = csv.reader(open('book.csv'))

for row in csv_data:
    cursor.execute('INSERT INTO booklist(id, name )VALUES(%s,%s)', row)
   # print(row)


mydb.commit()
cursor.close()
print("Done")