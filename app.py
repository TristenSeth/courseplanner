import flask 
from ec import *
app = flask.Flask(__name__)

@app.route('/getCourse/<query>/<quarter>')
def hello_world(query, quarter):
    courses = getCourseInfo("2021-2022", query, quarter)

    course_schedule = None
    ret = None
    for course in courses:
        curr = f'{course.subject} {course.code}'
        
        if curr  == query:
            #found course, get correct section
            for section in course.sections:
                #check for lec component and correct quarter
                if section.component == "LEC" and section.term.split(" ")[1] == quarter:
                    course_schedule = section.schedules[0]

                    ret = {
                        "response": {
                            "courseCode": f'{course.subject} {course.code}',
                            "courseName": str(course.title),
                            "schedule": str(course_schedule),
                            "minUnits": str(course.units_min),
                            "maxUnits": str(course.units_max)
                        }
                    }
    if ret is None:
        status_code = app.make_response(rv=({"response": f"No offering for {query} in {quarter}"}, 404, {}))
        return status_code
    return app.make_response(rv=(ret, 200, {}))

if __name__ == '__main__':
    app.run(port=5000)