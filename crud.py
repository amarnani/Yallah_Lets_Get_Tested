"""CRUD operations."""

from model import db, User, Facility, Professional, connect_to_db, Review

def create_user(email,password):
    """Create and return a new user"""

    user = User(email = email, password = password)

    db.session.add(user)
    db.session.commit()

    return user 

def get_user_by_id(user_id):

    user = User.query.filter(User.id == id).first()

    return user

def get_user():

    users = User.query.all()

    return users 

def get_user_by_email(email):

    user = User.query.filter(User.email == email).first()

    return user

def create_facility(facility_id, f_name_english, address_line_one, address_line_two_english,
                                        facility_category_name_english, website, email, telephone_1,
                                        lat, lng, area_english):

    facility = Facility(facility_id = facility_id, f_name_english = f_name_english, address_line_one = address_line_one, address_line_two_english=address_line_two_english,facility_category_name_english=facility_category_name_english,website=website, email=email, telephone_1=telephone_1, lat=lat, lng=lng, area_english=area_english)
    
    db.session.add(facility)
    db.session.commit()

    return facility

def get_facilities():

    facilities = Facility.query.all()
    return facilities

def create_professional(full_name_english, professionalcategoryid, 
                                            facility_id, facility_name_english,address_line_one,  
                                            address_line_two_english, address_line_two_arabic, 
                                            po_box, website, email_address, telephone,
                                            gender_english, lat, lng,
                                            area_english, nationality_english):
    # if we can get a facility by the id > make a proffessional else> skip person
    if Facility.query.filter_by(facility_id=facility_id).first():
        professional = Professional(full_name_english=full_name_english, professionalcategoryid = professionalcategoryid, facility_id=facility_id, facility_name_english=facility_name_english,address_line_one=address_line_one,address_line_two_english=address_line_two_english, 
                                    address_line_two_arabic=address_line_two_arabic, po_box = po_box, website=website, email_address=email_address, 
                                    telephone = telephone, gender_english = gender_english, lat = lat, lng = lng,
                                    area_english = area_english, nationality_english = nationality_english)


        db.session.add(professional)
        db.session.commit()

        return professional          

def get_allobgynv1():
    """ This will generate a table with facilities and doctors"""
    
    ##first find where this condition is true for facility for obgyn
    obgyn_facility_list = Facility.query.filter_by(facility_category_name_english='Obstetrics and Gynecology').all()
    #obgyn_facility_list.full_name_english
    for facility in obgyn_facility_list:
        print(facility.f_name_english)
        for professional in facility.professionals:
            print(professional.full_name_english)
    ##second inner join with professional table 
    #obgyn = db.session.query(obgyn_list.facility_id, Professional.facility_id).join(Professional).all()

    #session = Session()
    #obgyn = session.query(Facility).join(Professional, and_(Facility.facility_id==Professional.facility_id, Facility.facility_category_name_english == 'Obstetrics and Gynecology'), isouter=False)

    #return facility.f_name_english

def get_all_obgyn():
    """ This will generate a table with facilities and doctors"""
    
    ##first find where this condition is true for facility for obgyn
    obgyn_facility_list = Facility.query.filter_by(facility_category_name_english='Obstetrics and Gynecology').all()
    
    return obgyn_facility_list

def get_facility_by_id(facility_id):

    return Facility.query.get(facility_id)


def get_professional_by_id(id):

    return Professional.query.get(id)

def get_professional_by_id(professional_id):

    return Professional.query.get(professional_id)

def get_all_professionals():
    return Professional.query.all()

def get_all_obgyn_by_location_and_gender1(location, gender='all'):
    
    obgyns = db.session.query(Facility.facility_category_name_english,Professional.area_english, 
            Professional.full_name_english).filter(Facility.facility_category_name_english=='Obstetrics and Gynecology', Professional.area_english==location)
        ##add more attributes here 
        #obgyns = Professional.query.join(Facility).filter(Facility.facility_category_name_english=='Obstetrics and Gynecology', Professional.area_english==location).all()
        #print([(obgyn.facility.facility_category_name_english, obgyn.area_english) for obgyn in obgyns], '############ OBGYNS ############')
        
    if gender != 'all':
        obgyns = obgyns.filter(Professional.gender_english == gender)
        #obgyns = Professional.query.join(Facility).filter(Facility.facility_category_name_english=='Obstetrics and Gynecology', Professional.area_english==location, Professional.gender_english==gender).all()
        #print([(obgyn.facility.facility_category_name_english, obgyn.area_english, obgyn.gender_english) for obgyn in obgyns], '############ OBGYNS ############')
    #return db.session.query(Professional).filter_by(area_english=location, gender_english=gender).all()
    return obgyns.all()

def get_all_obgyn_by_location_and_gender(location, gender='all'):
    
    obgyns = db.session.query(Facility).filter(Facility.facility_category_name_english=='Obstetrics and Gynecology', Professional.area_english==location)
        ##add more attributes here 
        #obgyns = Professional.query.join(Facility).filter(Facility.facility_category_name_english=='Obstetrics and Gynecology', Professional.area_english==location).all()
        #print([(obgyn.facility.facility_category_name_english, obgyn.area_english) for obgyn in obgyns], '############ OBGYNS ############')
        
    if gender != 'all':
        obgyns = obgyns.filter(Professional.gender_english == gender)
        #obgyns = Professional.query.join(Facility).filter(Facility.facility_category_name_english=='Obstetrics and Gynecology', Professional.area_english==location, Professional.gender_english==gender).all()
        #print([(obgyn.facility.facility_category_name_english, obgyn.area_english, obgyn.gender_english) for obgyn in obgyns], '############ OBGYNS ############')
    #return db.session.query(Professional).filter_by(area_english=location, gender_english=gender).all()
    return obgyns.distinct()



def search_pro_by_gender(gender): 
    if gender == 'all':
        #return doctors_in_facilities.facility_id == doctors_in_professionals.facility_id
        return Professional.query.all()
    
    #return Professional.query.filter(Professional.gender_english == 'Female')
    #return Professional.query.filter_by(gender_english='Female').all()
    #return Professional.query.filter(Professional.employee_id, Professional.name).all()
    return db.session.query(Professional).filter_by(gender_english=gender).all()

def create_review(text, date_of_visit, stars, users):
    """Create and return a new review."""
    
    review = Review(text= text, date_of_visit= date_of_visit, stars=stars, users=users)
    
    db.session.add(review)
    db.session.commit()

    return review    