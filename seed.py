"""Utility file to seed ratings database from MovieLens data in seed_data/"""

import datetime
import os
import csv
#from sqlalchemy import func

from model import connect_to_db, db, User, Review, Facility, Professional
from server import app
import crud
os.system('dropdb doctors')
os.system('createdb doctors')
connect_to_db(app)
db.create_all()

with open('data/updated_facilities.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    facilities_in_db = []

    for row in reader: 
        facility_id = row['unique_id']
        f_name_english = row['f_name_english']
        address_line_one = row['address_line_one']
        address_line_two_english = row['address_line_two_english']
        facility_category_name_english = row['facility_category_name_english']
        website = row['website']
        email = row['email']
        telephone_1 = row['telephone_1']
        lat = row['x_coordinate']
        lng = row['y_coordinate']
        area_english = row['area_english']

        db_facility =crud.create_facility(facility_id, f_name_english, address_line_one, address_line_two_english, 
                                            facility_category_name_english, website, email, telephone_1, lat, lng, area_english)
        
        facilities_in_db.append(db_facility)  


##load all professionals files
with open('data/Sheryan_Professional_Detail.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    professionals_in_db = []

    for row in reader: 
        full_name_english = row['full_name_english']
        professionalcategoryid = row['professionalcategoryid']
        facility_id = int(row['facility_id'])
        facility_name_english = row['facility_name_english']
        #Facilities.query.filter_by(f_name_english = f_name_english).first().f_name_english
        address_line_one = row['address_line_one']
        address_line_two_english = row['address_line_two_english']
        address_line_two_arabic = row['address_line_two_arabic']
        po_box = row['po_box']
        website = row['website']
        email_address = row['email_address']
        telephone = row['telephone_1']
        gender_english = row['gender_english']
        lat = row['x_coordinate']
        lng = row['y_coordinate']
        area_english = row['area_english']
        nationality_english = row['nationality_english']

        db_professional =crud.create_professional(full_name_english, professionalcategoryid, 
                                            facility_id, facility_name_english,address_line_one,  
                                            address_line_two_english, address_line_two_arabic, 
                                            po_box, website, email_address, telephone,
                                            gender_english, lat, lng,
                                            area_english, nationality_english)
        
        professionals_in_db.append(db_professional)  


if __name__ == "__main__":
    connect_to_db(app)
