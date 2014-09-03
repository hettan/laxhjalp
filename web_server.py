from flask import Flask, render_template, request, session
app = Flask(__name__)

app.secret_key = 'lkfu5yDAS3dG2866645534sfsdfqFE13'

def logged_in():
    return "username" in session

def get_user():
    user = ""
    if logged_in():
        user = session["username"]
    return user

@app.route("/")
def index():
    return render_template("index.html", user=get_user())

@app.route("/info")
def info():
    return render_template("about.html", user=get_user())

@app.route("/prices")
def prices():
    return render_template("prices.html", user=get_user())

@app.route("/contact")
def contact():
    return render_template("contact.html", user=get_user())

def check_login(user, passw):
    return user == "admin" and passw == "admin"

@app.route("/login", methods=["POST"])
def login():
    user = request.form["user"]
    passw = request.form["passw"]
    print "user: %s passw: %s" % (user, passw)

    if check_login(user, passw):
        session["username"] = user
        return "True"

    else:
        return "False"
    
@app.route("/logout")
def logout():
    session.pop("username")
    return " "

if __name__ == "__main__":
    server_host = "0.0.0.0"
    app.run(debug=True,host=server_host)
