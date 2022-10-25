import mariadb

print("hij doet het naar de db")
        # mysql.connector
mydb = mariadb.connect(
  host="localhost",  #port erbij indien mac
 # port=8889,   # als je een mac hebt
  user="root",
  password="",  # als je een mac hebt
  database="havendb"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Kapitein")

myresult = mycursor.fetchall()

for x in myresult:
  print(x[2])

gaan = input("vul naam in")
sql = "INSERT INTO kapitein (naam, lengte) VALUES (%s, %s)"
val = (gaan, 21)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")