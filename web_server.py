# -*- coding: utf-8 -*-

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
    args = {}
    args["page"] = db.get_page("startsida")
    return render_body_wrapper("index.html", args)

@app.route("/info")
def info():
    args = {}
    args["page"] = db.get_page("info") 
    return render_body_wrapper("about.html", args)

@app.route("/prices")
def prices():
    args = {}
    args["page"] = db.get_page("priser") 
    return render_body_wrapper("prices.html", args)

@app.route("/contact")
def contact():
    args = {}
    args["page"] = db.get_page("kontakt") 
    return render_body_wrapper("contact.html", args)

@app.route("/rut_info")
def rut_info():
    args = {}
    args["page"] = db.get_page("rut_info") 
    return render_body_wrapper("rut_info.html", args)

@app.route("/interest_dialog")
def interest_dialog():
    return render_template("interest.html")

@app.route("/add_user_dialog")
def add_user_dialog():
    return render_template("create_user.html")

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
    return db.password_correct(email, passw)
#    return email == "admin" and passw == "admin"

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
        args = {}
        args["profile"] = db.get_profile_data(user)
        print args["profile"]
        return render_body_wrapper("edit_profile.html", args)

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

@app.route("/update_page", methods=["GET"])
def update_page():
    page = request.args.get("page")
    field = request.args.get("field")
    value = request.args.get("value")
    print page + field + value
#    page_name = "startsida"
 #   field = "carousel.first_slide.header"
  #  value = "new value yolo"

    user = get_user()
    if(is_admin(user)):
        if db.update_page_field(page, field, value):
            print "OK"
            return "OK"
        else:
            print "ERROR"
            return "ERROR"

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

@app.route("/create_user", methods=["POST"])
def create_user():
    user = get_user()
    if is_admin(user):
        email = request.form["email"]
        password = request.form["password"]
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        road = request.form["road"]
        road_number = request.form["road_number"]
        postal = request.form["postal"]
        city = request.form["city"]
        phone = request.form["phone"]
        admin = ("admin" in request.form)
        
        profile = Profile(email, password, first_name, last_name)
        profile.add_address(road, road_number, postal, city)
        if admin:
            profile.set_admin()

        if db.add_profile(profile):
            return users()

    return page_not_found()

@app.route("/change_password_dialog")
def change_password_dialog():
    return render_body_wrapper("change_password.html")

@app.route("/change_password", methods=["POST"])
def change_password():
    user = get_user()
    new_password = request.form["new_password"]
    old_password = request.form["old_password"]
    print "new_p = %s, old_p=%s old_p"
    return page_not_found()

@app.route("/reset_pages")
def reset_pages():
    user = get_user()
    if is_admin(user):
        db.clear_pages()
        db.setup_pages()
        return "OK"
    return page_not_found()

    
if __name__ == "__main__":
    server_host = "0.0.0.0"
    app.run(debug=True, host=server_host)
    reset_pages()
