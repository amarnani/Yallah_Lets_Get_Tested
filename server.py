"""Movie Ratings."""

from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session, jsonify, send_from_directory
from flask_debugtoolbar import DebugToolbarExtension
import crud


from model import connect_to_db, db, User, Review, Facility, Professional


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """View homepage."""
    
    obgyn_facility_list = crud.get_all_obgyn()


    return render_template('homepage.html', obgyn_facility_list = obgyn_facility_list)


@app.route('/users', methods = ["POST"])
def register_user():

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)

    if user:
        flash('User with this email already exists - try again with another email.')
    else:
        crud.create_user(email, password)
        flash('Account created - you can now log in')

    return redirect('/')

@app.route("/users/<user_id>")
def show_user(user_id):
    """Show details on a particular user."""

    user = crud.get_user_by_id(user_id)

    return render_template("user_details.html", user=user)

@app.route('/login', methods = ["POST"])
def process_login():

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)

    if user.password == password:

        session['user'] = user.email
        flash(f'You have sucessfully logged in {user.email}')
        return redirect('/')

    else:
        flash('The email or password you have entered is not valid')
        return redirect('/')

@app.route('/logout', methods = ['GET'])
def process_logout():

    if 'user' in session:
        del session['user']
    return redirect ('/')

@app.route('/facilities/<int:facility_id>')
def show_facility(facility_id):
    
    facility = crud.get_facility_by_id(facility_id)
    
    return render_template('facility_detail.html', facility = facility)

@app.route('/professionals/<int:professional_id>')
def show_professional(professional_id):
    
    professional = crud.get_professional_by_id(professional_id)
    
    return render_template('professional_detail.html', professional = professional)


@app.route("/")
def index():
    """Show homepage."""

    return render_template("index.html")


@app.route("/professionals/<int:professional_id>/ratings", methods=["POST"])
def create_review(professional_id):
    """Create a new rating for the movie."""

    logged_in_email = session.get("email")
    rating_score = request.form.get("stars")

    if logged_in_email is None:
        flash("You must log in to rate a Doctor.")
    elif not rating_score:
        flash("Error: you didn't select a score for your rating.")
    else:
        user = crud.get_user_by_email(email)
        proffessional = crud.get_professional_by_id(id)
        crud.create_review(text, date_of_visit, int(stars), users)

        flash(f"You rated this movie {stars} out of 5.")

    return redirect(f"/professionals/{id}")

# @app.route("/map/basic")
# def view_basic_map():
#     """Demo of basic map-related code.

#     - Programmatically adding markers, info windows, and event handlers to a
#       Google Map
#     - Showing polylines, directions, etc.
#     - Geolocation with HTML5 navigator.geolocate API
#     """

#     return render_template("map-basic.html")

    
@app.route("/map/docs")
def view_docs_map():
    """Show map of doctors."""

    return render_template("map-basic.html")

@app.route("/api/docs")
def doc_info():
     
    facility = crud.get_all_obgyn()

    facilities = [
         {
             "name": fac.f_name_english,
             "address":fac.address_line_one,
             "lat": fac.lat,
             "lng":fac.lng
             
         }
         for fac in facility
     ]
    return jsonify(facilities)

@app.route("/map/static/<path:resource>")
def get_resource(resource):
    return send_from_directory("static", resource)


# @app.route("/search-provider")
# def filter_providers():
#     return render_template("Search form.html", doctor_list=doctor_list)


@app.route("/search")
def show_doctors():
    
    gender = request.args.get('gender')
    location = request.args.get('location')
    print(gender)
    print(location)
    if gender and location: 
        obgyns = crud.get_all_obgyn_by_location_and_gender(location, gender)
        #doctor_list = crud.search_pro_by_gender(gender)
        print(obgyns, '$$$$$$$$$$$$$$$$$$ FROM SERVER $$$$$$$$$$$$$$$$$')
    else:
        obgyns = []

    return render_template("Search form.html", obgyns= obgyns)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be Trpe at the point
    # that we invoke the DebugToolbarExtension

    # Do not debug for demo
    ##IMPORTANT##
    ###TURN OFF WHEN DEPLOY###
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)
    #app.run(debug=True, use_reloader=False)
    app.run(host="0.0.0.0")
