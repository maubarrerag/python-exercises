import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.webucator.com/course-demos/python/courselist.cfm'
headers = {'user-agent': 'my-app/0.0.1'}

course_search = input('Enter your search text (e.g., "Python") : ')
r = requests.get(url, headers=headers)
content = r.text

soup = BeautifulSoup(content, 'html.parser')
courses = soup.find_all('td', {'class': 'CourseName'}, 
    text=re.compile(course_search))

if len(courses)  == 0 :
    print('No courses were found')
    exit

for i, courses in enumerate(courses, 1):
    print(i, courses.text.strip())
print('-'*70)

# Challenge:
# List the 3 most common Category Group names

from collections import Counter

cat_groups = soup.find_all('td', {'class': 'CategoryGroup'})
c = Counter(cat_groups)
print('The 3 most common Category Groups')
print(c.most_common(3))
print('-'*70)