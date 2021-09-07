from explorecourses import *
from explorecourses import filters

def getCourseInfo(yearOffered, courseQuery, quarter):
    connect = CourseConnection()
    courses = connect.get_courses_by_query(courseQuery, quarter.toUpper(), year=yearOffered)

    return courses


