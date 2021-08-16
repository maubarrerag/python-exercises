# The Requests Library
import requests

url = 'https://www.webucator.com/course-demos/python/courselist.cfm'
r = requests.get(url)
content = r.text
print(content[:200]) # print first 200 characters

# Beautiful Soup
from bs4 import BeautifulSoup
import re

soup = BeautifulSoup(content, 'html.parser')

# Find all <a> tags
links = soup.find_all('a')
print('All <a> tags using Beautiful soup:', len(links), 
    '-'*70, sep='\n')

# Find all tags that begin with "s" (script, style, span, etc.)
t_tags = soup.find_all(re.compile('^s'))
print('All tags that begin with "s":', 
    len(t_tags), '-'*70, sep='\n')

# Find all <link> tags with rel attribute
links = soup.find_all('link', {'rel': True})
print('All <link> tags with rel attribute:', 
    len(links), '-'*70, sep='\n')



# Find all <td> tags with a class attribute value of "CourseName"
td_class = soup.find_all('td', {'class': 'CourseName'})
print('All <td> tags with a class attribute value of "CourseName":', 
    len(td_class), '-'*70, sep='\n')

# Find a phone number formatted as "###-###-####"   
phones = soup.find_all(text = re.compile('\d{3}-\d{3}-\d{4}')) 
print('''Find a phone number 
    formatted as "###-###-####"''', 
    phones, '-'*70, sep='\n')

# Find the first three <td> tags that contain text that 
# ends with "Getting Started"
projects_in_tds = soup.find_all('td', 
    text = re.compile('Getting Started$'), limit=3)
print('''Find the first three <td> tags that contain text that 
    ends with "Getting Started"''', 
    projects_in_tds, '-'*70, sep='\n')

# Find all <a> tags that have an href attribute
links_with_href = soup.find_all('a', href=True)
print('Find all <a> tags that have an href attribute', 
    len(links_with_href), '-'*70, sep='\n')

# Find all <a> tags that have an href attribute 
# that contains "testamonials.cfm"
internal_links = soup.find_all('a', 
    href = re.compile('testimonials.cfm'))
print('''Find all <a> tags that have an href attribute 
    that contains "testimonials.cfm''', 
    len(internal_links), '-'*70, sep='\n')

# Find the <td> tags that contain "Java "   
advanced = soup.find_all('td', text = re.compile('Java '))
print('''Find the the courses that contain "Java " ''', 
    advanced, '-'*70, sep='\n')

# Find the <td> tags that contain "JavaS"  (e.g., JavaScript)
advanced = soup.find_all('td', text = re.compile('JavaS'))
print('''Find the the courses that contain "JavaS" ''', 
    advanced, '-'*70, sep='\n')

# Find the <td> tags that contain "Java " or "JavaS"  (e.g., JavaScript)
advanced = soup.find_all('td', text = re.compile('Java[ |S]'))
print('''Find the the courses that contain "Java " or JavaS" ''', 
    advanced, '-'*70, sep='\n')

# The select() Method 
top_nav_links = soup.select('ul.nav li a')
print('Elements based on CSS selectors')
for link in top_nav_links:
    print(link.text.strip()) 
print('-'*70)  

# Put it all Together: Output List of Course Names
url = 'https://www.webucator.com/course-demos/python/courselist.cfm'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
content = r.text

soup = BeautifulSoup(content, 'html.parser')
course_names = soup.select('td.CourseName')
print('All Courses')
for i, course_name in enumerate(course_names, 1):
    print(i, course_name.text.strip()) 
print('-'*70) 

# Using XML: Output List of Course Names
url='https://www.webucator.com/course-demos/python/courselistxml.cfm'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
content = r.text

soup = BeautifulSoup(content, 'xml')
course_names = soup.find_all('title')
print('All Courses using XML')
for i, course_name in enumerate(course_names, 1):
    print(i, course_name.text) 
print('-'*70)