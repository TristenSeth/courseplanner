from explorecourses import *
from explorecourses import filters





def getCourseInfo(yearOffered, courseQuery, quarter):
    connect = CourseConnection()
    courses = connect.get_courses_by_query(courseQuery, quarter.toUpper(), year=yearOffered)

    #find correct course
    
    # for course in courses:
    #     code = f'{course.subject} {course.code}'
    #     if courseQuery == code:
    #         #found
    #         courseName = str(course.title)
    #         maxUnits = str(course.units_max)
    #         minUnits= str(course.units_min)
    #         sections = course.sections
    #         courseData = {
    #             "name": courseName,
    #             "code": code,
    #             "maxUnits": maxUnits,
    #             "minUnits": minUnits,
    #             "sections": sections
    #         }
    return courses

# getCourseInfo("2021-2022", "CS 110", filters.AUTUMN)
