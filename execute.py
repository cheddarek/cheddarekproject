from flask import Flask , render_template ,redirect , url_for , request 
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="cheddarek" 
)
mycursor = mydb.cursor()


app = Flask(__name__)
#page d  acceuil
@app.route("/")
def home():							
    return render_template("Inscription.html")




#register 
@app.route("/register",methods=["POST","GET"])
def register():
    if request.method == "POST":
        nom = request.form["Nom"]
        prenom = request.form["Prenom"]
        email =  request.form["email"]
        contact =  request.form["contact"]
        password = request.form["password"]
        lieu = request.form["lieu"] 
        mytype = request.form["type"]  
        if mytype == "Client":
            mtype= 1 	
        if mytype == "Vendeur":
            mtype= 2 	
        sql = "INSERT INTO users(`firstName`, `secondName`, `mail`, `psw`, `phone`,`adresse`, `userType`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val = (prenom, nom, email  , password , contact , lieu , mtype)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect(url_for("user",usr=email))
    else: 
        return render_template("Inscription.html")

#login 
@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == "POST":
        email =  request.form["email"]
        password = request.form["password"] 
        sql = "SELECT * from users where mail= %s and psw= %s"
        val = (email, password)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        return redirect(url_for("user",usr=email))
    else: 
        return render_template("Login.html")

# pour tester 
@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"	
if __name__ == "__main__":
    app.run(debug=True)
