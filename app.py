from flask import Flask
import mariadb
from flask_cors import CORS

app = Flask(__name__)

mydb = mariadb.connect(
  host="localhost",  #port erbij indien mac
 # port=8889,   # als je een mac hebt
  user="root",
  password="",  # als je een mac hebt
  database="havendb"
)


CORS(app)

@app.route("/allekapiteinen")
def hello_world():
    eindString = ""
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Kapitein")
    myresult = mycursor.fetchall()
    for x in myresult:
        eindString += "<div>"+x[2]+"</div>"
    return eindString