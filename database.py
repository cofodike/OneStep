import pymongo
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient["mydatabase"]
dblist = myclient.list_database_names()

#a collection in mongo is the equvalent of a table in sql
course_collection = mydb['course_schedule']

def add_course():

    course_dict = {}
    course_id = input('Please enter course id: ')
    course_room = input('Please enter course room: ')
    start_time = input('Please enter start time: ')
    end_time = input('Please enter end time: ')

    course_dict['course_id'] = course_id
    course_dict['Course room'] = course_room
    course_dict['Start time'] = start_time
    course_dict['End timme'] = end_time
    return course_dict

def drop_course(course_to_drop):
    #the idea here is to run through the entire course_collection it is done w the find() method
    #there's a problem with this course
    for course in course_collection.find():
        for key,value in course.items():
            if key == 'course_id' and value == course_to_drop:
                del course

        
def print_courses():
    for course in course_collection.find():
        print(course)

def empty_class_collection():
     dropped = course_collection.drop()
     if dropped == True:
         return 'Successfully emptied'
     else:
         return 'Unsuccessful'

print(' A: Insert a new course, \n B: Drop a course, \n C: Print out database, \n D: Wipe database ')
user_choice = input('Enter an option: ' )
user_choice = user_choice.upper()

if user_choice == 'A':
    course_list = course_collection.insert_one(add_course())
elif user_choice == 'B':
    course_to_drop = input('Please enter course_id: ')
    #to drop a choice, we use a dictionary syntax
    #therefore we have to find the right course by searching the dictionary for the right key:
    drop_course(course_to_drop)
elif user_choice == 'C':
    print_courses()
elif user_choice == 'D':
    print('Are you sure you want to proceed? This cannot be undone: ')
    confirmation = input('Type "YES" to proceed or anything else to be returned to main menu: ')
    if confirmation == 'YES':
        empty_class_collection()
    else:
        print(' A: Insert a new course, \n B: Drop a course, \n C: Print out database, \n D: Wipe database ')
        user_choice = input('Enter an option: ' )
