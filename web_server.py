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

def render_body_wrapper(child_page, args=None):
    user = get_user()
    admin = is_admin(user)

    return render_template(child_page, user=user, admin=admin)

@app.route("/")
def index():
    return render_body_wrapper("index.html")

@app.route("/info")
def info():
    return render_body_wrapper("about.html")

@app.route("/prices")
def prices():
    return render_body_wrapper("prices.html")

@app.route("/contact")
def contact():
    return render_body_wrapper("contact.html")

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

def is_admin(user):
    return len(user) > 0

@app.errorhandler(404)
def page_not_found(e=None):
    return render_template("404.html"), 404

@app.route("/admin")
def admin():
    user = get_user()
    if len(user) > 0:
        if(is_admin(user)):
            return render_body_wrapper("admin.html")

    return page_not_found()

@app.route("/settings")
def settings():
    user = get_user()
    if len(user) > 0:
        return render_body_wrapper("settings.html")

    return page_not_found()
    

if __name__ == "__main__":
    server_host = "0.0.0.0"
    app.run(debug=True,host=server_host)
