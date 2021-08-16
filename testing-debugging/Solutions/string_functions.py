import random
import string
import re

def prepend(s,c):
    return c + s

def append(s,c):
    return s + c

def insert(s,c,pos):
    return s[0:pos] + c + s[pos:]

def remove_non_ascii_letters(text):
    cleaned_text = ''
    for char in text:
        if char in string.ascii_letters:
            cleaned_text += char
    return cleaned_text

def discover_email(email):
    email = re.sub(r'\W+at\W+','@',email)
    email = re.sub(r'\W+dot\W+','.',email)
    return email

def inits(name):
    inits = []
    for name_part in name.split():
        inits.append(name_part[0])
    return '.'.join(inits) + '.'