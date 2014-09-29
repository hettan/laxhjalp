from flask import Flask, render_template, request, session, redirect

from mongo_database_handler import MongoDatabaseHandler
from profile import Profile
 
app = Flask(__name__)
app.secret_key = 'lkfu5yDAS3dG2866645534sfsdfqFE13'

db = MongoDatabaseHandler()
db.clear_pages()
db.setup_pages()
db.setup_pages()
def logged_in():
    return "username" in session

def get_user():
    user = ""
    if logged_in():
        user = session["username"]
    return user

def render_body_wrapper(child_page, args={}):
    user = get_user()
    admin = is_admin(user)
    if admin:
        args["unread_interest_count"] = db.get_all_unread_interests().count()

    return render_template(child_page, user=user, admin=admin, args=args)

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

@app.route("/interest_dialog")
def interest_dialog():
    return render_template("interest.html")

@app.route("/interest", methods=["POST"])
def interest():
    email = request.form["email"]
    name = request.form["name"]
    address = request.form["address"]
    phone = request.form["phone"]
    help_with = request.form["help_with"]
    start_date = request.form["start_date"]

    if db.add_interest(email, name, address, phone,
                       help_with, start_date):
        return redirect("/", code=302)
    return page_not_found()
    
def check_login(email, passw):
#    return db.password_correct(email, passw)
    return email == "admin" and passw == "admin"

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

@app.route("/show_profile/<user>")
def show_profile(user):
    user_logged_in = get_user()
    if is_admin(user_logged_in):
        args = {}
        args["profile"] = db.get_profile_data(user)
        return render_body_wrapper("edit_profile.html", args)
    else:
        return page_not_found()

@app.route("/settings")
def settings():
    user = get_user()
    if len(user) > 0:
        return render_body_wrapper("settings.html")

    return page_not_found()
    
@app.route("/edit_text", methods=["GET"])
def edit_text():
    page = request.args.get("page")
    user = get_user()
    if(is_admin(user)):
        args = {}
        args["page"] = db.get_page(page)
        print args
        return render_body_wrapper("change_text.html", args)
    else:
        return page_not_found()

@app.route("/users")
def users():
    #for profile in Profile.dummy_profiles():
    #    db.add_profile(profile)
    user = get_user()
    if(is_admin(user)):
        args = {}
        args["users"] = db.get_all_profiles()
        return render_body_wrapper("users.html", args)
    else:
        return page_not_found()

@app.route("/edit_profile", methods=["GET"])
def edit_profile():
    email = request.args.get("email")
    field = request.args.get("field").strip()
    value = request.args.get("value")
    
    user = get_user()
    if(email == user or is_admin(user)):
        if db.change_profile(email, field, value):
            return "True"
        else:
            return "False"

def cursor_to_list(cursor):
    l = []
    for elem in cursor:
        l.append(elem)
    return l

#Unread at the top
def sorted_interests(unread_interests, all_interests):
    unread_interests = cursor_to_list(unread_interests)
    all_interests = cursor_to_list(all_interests)
    for unread in unread_interests:
        all_interests.remove(unread)
    return unread_interests + all_interests

@app.route("/show_interests", methods=["GET"])
def show_interests():
    user = get_user()
    if is_admin(user):
        args = {}
        unread_interests = db.get_all_unread_interests()
        all_interests = db.get_all_interests()
        args["interests"] = sorted_interests(unread_interests,
                                             all_interests) 
        return render_body_wrapper("show_interests.html", args)
    else:
        return page_not_found()

@app.route("/set_interest_read", methods=["GET"])
def set_interest_read():
    interest_id = request.args.get("id")
    value = request.args.get("value")
    user = get_user()
    if is_admin(user):
        if db.set_interest_read(interest_id, value):
            return "OK"
        else:
            return "FAILED"
    else:
        return page_not_found()

if __name__ == "__main__":
    server_host = "0.0.0.0"
    app.run(debug=True,host=server_host)
