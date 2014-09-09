from flask import Flask, render_template, request, session, redirect

from mongo_database_handler import MongoDatabaseHandler
from profile import Profile
 
app = Flask(__name__)
app.secret_key = 'lkfu5yDAS3dG2866645534sfsdfqFE13'

db = MongoDatabaseHandler()

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

def body_wrapper_message(msg):
    user = get_user()
    admin = is_admin(user)
    
    return render_template("message.html", msg=msg, user=user, admin=admin)

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

@app.route("/rut_info")
def rut_info():
    return render_body_wrapper("rut_info.html")

@app.route("/register_dialog")
def register_dialog():
    return render_template("register.html")

@app.route("/interest", methods=["POST"])
def interest():
    email = request.form["email"]
    name = request.form["name"]
    phone = request.form["phone"]
    help_with = request.form["message"]
    start_date = request.form["start_date"]
    #insert info a new mongodb collection interests
    return redirect("/", code=302)

@app.route("/register", methods=["POST"])
def register():
    email = request.form["email"]
    password = request.form["password"]
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    #return "%s %s %s %s"%(email,password,first_name,last_name)
    profile = Profile(email, password, first_name, last_name)
    if db.add_profile(profile):
        session["username"] = profile.email
        
        msg = "Registrering klar!"
    else:
        msg = "Registreringen misslyckades, var god fk igen."
    return redirect("/", code=302)
    
def check_login(email, passw):
    return db.password_correct(email, passw)
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

@app.route("/reset")
def reset(email):
    return "RESET %s" % email

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
