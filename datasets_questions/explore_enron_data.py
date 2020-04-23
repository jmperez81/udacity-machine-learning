#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
print("Number of persons in dataset : ", len(enron_data))
print("Persons in dataset : ", enron_data.keys())
print("Number of features per person : ", len(enron_data["METTS MARK"]))

number_poi = 0
number_poi_with_unknown_total_payments = 0
number_people_with_salary = 0
number_known_emails = 0
number_people_without_defined_total_payments = 0
for person in enron_data:
    if enron_data[person]['poi'] == True:
        number_poi = number_poi + 1
        if enron_data[person]['total_payments'] == 'NaN':
            number_poi_with_unknown_total_payments = number_poi_with_unknown_total_payments + 1
    if enron_data[person]['salary'] != 'NaN':
        number_people_with_salary = number_people_with_salary + 1
    if enron_data[person]['email_address'] != 'NaN':
        number_known_emails = number_known_emails + 1
    if enron_data[person]['total_payments'] == 'NaN':
        number_people_without_defined_total_payments = number_people_without_defined_total_payments + 1
print("Number of persons of interest : ", number_poi)
print("Stock for James Prentice : ", enron_data["PRENTICE JAMES"]["total_stock_value"])
print("Emails from Wesley Colwell to POI : ", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])
print("Stock options for Jeffrey K Skilling : ", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])
print("People with defined salary : ", number_people_with_salary)
print("Known emails : ", number_known_emails)
print("People without defined total payments : ", number_people_without_defined_total_payments, " which is percentage : ", (number_people_without_defined_total_payments * 100) / len(enron_data))
print("POI without defined total payments : ", number_poi_with_unknown_total_payments, " which is percentage : ", (number_poi_with_unknown_total_payments * 100) / len(enron_data))