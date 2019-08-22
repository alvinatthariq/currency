import pymysql
from flask import Flask,render_template,request,redirect,flash,jsonify


connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='shopee',
)

app = Flask(__name__)
app.secret_key = 'secret'


@app.route("/")
def home():
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM currency"
            try:
                cursor.execute(sql)
                result = cursor.fetchall()
                resp = jsonify(result)
                print(type(resp))
                resp.status_code = 200
                return resp

    
            except:
                flash("Oops! Something wrong")
    
        connection.commit()
    finally:
        print("sukses")

    return render_template("home.html",data=result)

@app.route("/insert", methods=["GET", "POST"])
def add():
    if request.method == 'POST':
        json = request.json()
        cur_from = json['cur_from']
        cur_to = json['cur_to']

    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO currency ('cur_from', 'cur_to') VALUES (%s, %s)"
            try:
                cursor.execute(sql, (cur_from,_ur_to))
                flash("Data added successfully")
            except:
                flash("Oops! Something wrong")
    
        connection.commit()
    finally:
        print('Continue')
        
    

    return redirect("/")


		

if __name__ == "__main__":
    app.run(debug=True)
    

