"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""
from flask import Flask

from model import *

app = Flask(__name__)
connect_to_db(app)

# -------------------------------------------------------------------
# Start here.
Chev = db.session.query(Brand).first()
#s = query_brand.filter(id=14).all()
print Chev.name
# Part 2: Write queries

# Get the brand with the **id** of 8.
s = Brand.query.get(8)
print s

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.

records = Model.query.filter_by(brand_name='Chevrolet', name='Corvette').all()
print records
# for s in records:
# 	print s.id,s.year,s.brand_name,s.name

# Get all models that are older than 1960.
records = Model.query.filter(Model.year < 1960).all()
#print records
# for s in records:
# 	print s.id,s.year,s.brand_name,s.name

# Get all brands that were founded after 1920.

records = Brand.query.filter(Brand.founded < 1920).all()
#print records
# Get all models with names that begin with "Cor".

records = Model.query.filter(Model.name.like("%Cor%")).all()
for s in records:
	print s

# Get all brands with that were founded in 1903 and that are not yet discontinued.
records = Brand.query.filter_by ( founded = 1903 , discontinued = None )
for s in records:
	print s

# Get all brands with that are either discontinued or founded before 1950.

#records = Brand.query.filter_by(or_(founded < 1950, discontinued != NONE )).all()

#db.users.filter(or_(db.users.name=='Ryan', db.users.country=='England'))

# Get any model whose brand_name is not Chevrolet.

records = Model.query.filter(Model.brand_name.notlike("Chevrolet")).all()
#for s in records:
#	print s

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):

	'''Takes in a year, and prints out each model, brand_name, and brandheadquarters for that year using only ONE database query.'''

	model_result = db.session.query(Model.name,
                        Model.brand_name,
                        Brand.headquarters).join(Brand).filter(Model.year == year)

	return model_result

model_results = get_model_info(1957)

print model_results.all()    # [(n, d, p), (n, d, p)]


def get_brands_summary():
 	
 	brand_result = db.session.query(Model.name,
                        Model.brand_name)

	return brand_result

brand_results = get_brands_summary()

print brand_results.all()      # [(n, d, p), (n, d, p)]


# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):

	join_cond = "%"+mystr+"%"
	print join_cond

 	brand_result = db.session.query(Brand.id,
                        Brand.name,Brand.founded,Brand.headquarters,Brand.discontinued).filter(Brand.name.like(join_cond))
	return brand_result

brand_results = search_brands_by_name ("Chev")

print brand_results.all()

def get_models_between(start_year, end_year):

 	model_result = db.session.query(Model.id,
                        Model.name,Model.brand_name,Model.year).filter(Model.year >= start_year, Model.year <= end_year )
	return model_result

model_results = get_models_between (1900,1960)

print model_results.all()      # [(n, d, p), (n, d, p)]
   

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
#It returns object which contains the result set. When i do the type of it below , it is a object of class flask_sqlachemy
# type(Brand.query.filter_by(name='Ford'))
#<class 'flask_sqlalchemy.BaseQuery'>

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
# Association store relationships between two tables. 
# For example : Essence_consumption is an association table between Skesis and the Prisoner tables.



