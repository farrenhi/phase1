from flask import Flask, request, render_template, redirect, url_for, session

### Python-SQL
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345678",
  database='website'
)
###

app = Flask(
    __name__,
    static_folder="",
    static_url_path="/",
)

app.secret_key = "secret" # session would need this!

@app.route("/") # , methods=["GET"]
def index():
    return render_template("index.html")

### Python SQL function
def get_info_from_sql(username):
    '''input username and return corresponding info from SQL'''
    mycursor = mydb.cursor()

    sql = "SELECT * FROM member WHERE username = (%s)"
    val = (username,)
    mycursor.execute(sql, val)

    myresult = mycursor.fetchall()
    if myresult:
        return myresult[0]
    else:
        return None

def commit_info_into_sql(name, username, password):
    '''this function would write data into SQL database'''
    mycursor = mydb.cursor()

    sql = "INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
    val = (name, username, password)
    mycursor.execute(sql, val)

    mydb.commit()
    
    # return redirect(url_for("index"))
    # Question: if it is commit, we will go to index directly. but how to design it?
    # in case if database writing does not work, we should show error message about database

def get_all_messages_from_sql():
    mycursor = mydb.cursor()
    mycursor.execute(
      # "SELECT message.*, member.name FROM message INNER JOIN member ON message.member_id = member.id;"
      "SELECT message.content, member.name FROM message INNER JOIN member ON message.member_id = member.id;"
    )
    myresult = mycursor.fetchall()
    return myresult    

def commit_to_sql_message(member_id, content):
    '''this function would write data into SQL database Table message'''
    mycursor = mydb.cursor()

    sql = "INSERT INTO message (member_id, content) VALUES (%s, %s)"
    val = (member_id, content)
    mycursor.execute(sql, val)

    mydb.commit()  

###

# Registration Endpoint
@app.route("/signup", methods=["POST"])
def signup():
    name = request.form["name"]
    username = request.form["username"]
    password = request.form["password"]
    
    # check if any username info in SQL
    if get_info_from_sql(username) is not None:
        return redirect(url_for("error", message="Username is registered!"))
    else:
        commit_info_into_sql(name, username, password)
        return redirect(url_for("index"))
        # return redirect(url_for("error", message="Database is not accessible!"))
        # return """<h1> This is the new username! </h1>"""


# Create Message Endpoint
@app.route("/createMessage", methods=["POST"])
def createMessage():
    content = request.form["message"]
    member_id = session.get("id")
    commit_to_sql_message(member_id, content)
    return redirect(url_for("member"))

# Verification Endpoint
@app.route("/signin", methods=["POST"])
def signin():
    username = request.form["username"]
    password = request.form["password"]
    if username == '' or password == '':
        message_info = "Please enter username and password"
        return redirect(url_for("error", message=message_info))
    
    ## We need to go to SQL to get the password info
    user_info_from_sql = get_info_from_sql(username)
    password_from_sql = user_info_from_sql[3]
        
    if password == password_from_sql:
        session["SIGNED-IN"] = True  # Set the "SIGNED-IN" state to True in the session.
        session["id"] = user_info_from_sql[0]
        session["name"] = user_info_from_sql[1]
        session["username"] = username
        session["password"] = password
        session["follower_count"] = user_info_from_sql[4]
        session["time"] = user_info_from_sql[5]
       
        # , message_data=messages_for_board
        return redirect(url_for("member"))
    else:
        message_info = "Username or password is not correct"
        return redirect(url_for("error", message=message_info))

@app.route("/member")
def member():
    if session.get("SIGNED-IN"):
        # User is signed in, render the success page.

        messages_for_board = get_all_messages_from_sql()
        name = session.get("name")
        return render_template("member.html", data=name, message_data=messages_for_board)
    else:
        # User is not signed in, redirect to the login page or show an error message.
        return redirect(url_for("index"))  # Redirect to the login page if not signed in.

@app.route("/error")
def error():
    data_received = request.args.get("message")
    return render_template("error.html", data=data_received)

@app.route("/square/<int:num>", methods=["GET"])
def square(num):
    # Get method: this does not show up in the URL
    #maxNumber = request.args.get("max", "")
    
    # Post method: you need to use request! This method is good for privacy
    # maxNumber = request.form["max"]
    # maxNumber = int(maxNumber)
    result = num * num

    # "Result:" + str(result)
    return render_template("result.html", data=result)

@app.route('/signout', methods=["GET"])
def signout():
    session["SIGNED-IN"] = False 
    session.pop('username', None)  # Remove the username from the session
    session.clear()  # Clear all session data
    return redirect(url_for('index'))

# run server
app.run(port=3000)
