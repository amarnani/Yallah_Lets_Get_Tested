"""Models and database functions for Ratings project."""

from flask_sqlalchemy import SQLAlchemy
from collections import defaultdict

# This is the connection to the PostgreSQL database; we're getting
# this through the Flask-SQLAlchemy helper library. On this, we can
# find the `session` object, where we do most of our interactions
# (like committing, etc.)

db = SQLAlchemy()

#####################################################################
# Model definitions
class User(db.Model):

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                    autoincrement=True,
                    primary_key=True,
                    )
    email = db.Column(db.String, nullable=True)
    password = db.Column(db.String, nullable=True)

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'

class Review (db.Model):
    """ All Reviews """
    __tablename__ = 'reviews'

    review_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True)

    facility_id = db.Column(db.Integer, db.ForeignKey('facilities.facility_id'))
    user_id  = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    text = db.Column(db.String)
    date_of_visit = db.Column(db.Integer)
    stars = db.Column(db.Integer)

    users = db.relationship('User', backref='reviews')
    facility = db.relationship('Facility', backref='reviews')


class Facility(db.Model):
    """ Medical Facilities"""

    __tablename__ = "facilities"

    facility_id = db.Column(db.Integer, primary_key = True)
    f_name_english = db.Column(db.String(200), nullable=True)
    address_line_one = db.Column(db.String(300), nullable=True)
    address_line_two_english = db.Column(db.String(300), nullable=True)
    facility_category_name_english = db.Column(db.String(300), nullable=True)
    website = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True)
    telephone_1 = db.Column(db.String(200), nullable=True)
    lat = db.Column(db.String(30), nullable=True)
    lng = db.Column(db.String(30), nullable=True)
    area_english = db.Column(db.String, nullable=True)
    

    def __repr__(self):
        """Provide helpfulrepresenation when printed."""

        return f"<Facility id={self.facility_id} f_name_english={self.f_name_english} >"

class Professional(db.Model):
    """ All Docs """

    __tablename__ = 'professionals'

    id = db.Column(db.Integer, 
                    autoincrement = True,
                    primary_key = True,
                    )
    full_name_english = db.Column(db.String, nullable=False)
    professionalcategoryid = db.Column(db.String(3), nullable=True)
    facility_id = db.Column(db.Integer, db.ForeignKey('facilities.facility_id'), nullable=True)
    facility_name_english = db.Column(db.String(300), nullable=False)
    address_line_one = db.Column(db.String(300), nullable=True)
    address_line_two_english = db.Column(db.String(300), nullable=True)
    address_line_two_arabic = db.Column(db.String(300), nullable=True)
    po_box = db.Column(db.String, nullable = True)
    website = db.Column(db.String(300), nullable = True)
    email_address = db.Column(db.String(200), nullable = True)
    telephone = db.Column(db.String(200), nullable = True)
    gender_english = db.Column(db.String(50), nullable = True)
    lat = db.Column(db.String(30), nullable=True)
    lng = db.Column(db.String(30), nullable=True)
    area_english = db.Column(db.String(300), nullable = True)
    nationality_english = db.Column(db.String(100), nullable = True)

    facility = db.relationship('Facility', backref='professionals')

#####################################################################
# Helper functions


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///doctors'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will
    # leave you in a state of being able to work with the database
    # directly.

    from server import app
    connect_to_db(app)
    print("Connected to DB.")




    