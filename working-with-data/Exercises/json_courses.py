import requests

data="https://www.webucator.com/course-demos/python/courselistjson.cfm" 

r = requests.get(data)
courses = r.json()

# Finish the code