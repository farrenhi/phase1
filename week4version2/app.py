from flask import Flask, request, render_template, redirect, url_for, session

app = Flask(
    __name__,
    static_folder="",
    static_url_path="/",
)

app.secret_key = "secret" # session would need this!

@app.route("/") # , methods=["GET"]
def index():
    return render_template("index.html")

# Verification Endpoint
@app.route("/signin", methods=["POST"])
def signin():
    username = request.form["username"]
    password = request.form["password"]
    if username == '' or password == '':
        message_info = "Please enter username and password"
        return redirect(url_for("error", message=message_info))
        
    if username == 'test' and password == 'test':
        session["SIGNED-IN"] = True  # Set the "SIGNED-IN" state to True in the session.
        session["username"] = username
        return redirect(url_for("member"))
    else:
        message_info = "Username or password is not correct"
        return redirect(url_for("error", message=message_info))

@app.route("/member")
def member():
    if session.get("SIGNED-IN"):
        # User is signed in, render the success page.
        return render_template("member.html")
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
    # remove the username from the session if it's there
    username = session["username"]
    session.pop('username', None)
    return redirect(url_for('index'))

# run server
app.run(port=3000)
