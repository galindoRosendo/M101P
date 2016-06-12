import pymongo
import datetime
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# add a review date to a single record using update_one
def viewOneStudentHW(student_id):

    print "Show one student"
    # get a handle to the school database
    db=connection.school
    students = db.students

    try:
        # get the doc
        score = students.find_one({'_id':student_id})
        print "Student: ", score

    except Exception as e:
        raise

viewOneStudentHW(137)
viewOneStudentHW(138)
viewOneStudentHW(139)
viewOneStudentHW(140)
