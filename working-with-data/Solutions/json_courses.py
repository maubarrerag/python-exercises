import requests

data="https://www.webucator.com/course-demos/python/courselistjson.cfm" 

r = requests.get(data)
courses = r.json()

for i, course in enumerate(courses, 1):
    print(i, '{} / {} / {}'.format(course['CourseName'],
                course['Category'],
                course['CategoryGroup']))
print('-' * 70)