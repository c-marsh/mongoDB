import pymongo
import os

MONGO_URI = os.environ['MONGO_URI']
DBS_NAME = "myFirstMDB"
COLLECTION_NAME = "myFirstMDB"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to Mongo: %s") % e


def show_menu():
    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Modify a Record")
    print("4. Delete a record")
    print("5. Exit")

    option = input("Enter option: ")
    return option


def get_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    try:
        doc = coll.find_one({'first': first.lower(),
                             'last': last.lower()})
    except:
        print("Error accessing database")
    if not doc:
        print("")
        print("no results found!")
    return doc


def add_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    dob = input("Enter date of birth > ")
    gender = input("Enter gender > ")
    hair_colour = input("Enter hair colour > ")
    occupation = input("Enter occupation > ")
    nationality = input("Enter nationality > ")

    new_doc = {'first': first.lower(),
               'last': last.lower(),
               'dob': dob,
               'gender': gender,
               'hair_colour': hair_colour,
               'occupation': occupation,
               'nationality': nationality}

    try:
        coll.insert(new_doc)
        print("")
        print("Document insert!")
    except:
        print("Error accessing database")


def find_record():
    doc = get_record()
    if doc:
        print("")
        for key, value in doc.items():
            if key != "_id":
                print(key.capitalize() + ": " + value.capitalize())


def edit_record():
    doc = get_record()
    if doc:
        update_doc={}
        print("")
        for key, value in doc.items():
            if key != "_id":
                update_doc[key] = input(key.capitalize() + " [" + value + "] > ")
                if update_doc[key] == "":
                    update_doc[key] = value
        try:
            coll.update_one(doc, {'$set': update_doc})
            print("")
            print("Document updated!")
        except:
            print("Error accessing database")


def delete_record():
    doc = get_record()
    if doc:
        print("")
        for key, value in doc.items():
            if key != "_id":
                print(key.capitalize() + ": " + value.capitalize())
        print("")
        confirmation = input("Is this the record you wish to delete? \n(Y/N)")

        if confirmation.lower() == 'y':
            try:
                coll.delete_one(doc)
                print("Record deleted!")
            except:
                print("Error accessing the Database")
        else:
            print("Record has not been deleted")


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            print("You have selected option 1")
            add_record()
        elif option == "2":
            print("You have selected option 2")
            find_record()
        elif option == "3":
            print("You have selected option 3")
            edit_record()
        elif option == "4":
            print("You have selected option 4")
            delete_record()
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid Option")
        print("")


conn = mongo_connect(MONGO_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

main_loop()