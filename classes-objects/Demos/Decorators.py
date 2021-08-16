def foo(f):
    print(f)
    def foo_inner():
        pass
    return foo_inner
    
def bar():
    pass

# Create a decorator:

print(bar)
bar = foo(bar)
print(bar)

'''from datetime import datetime

def format_report(f):
    def inner(text):
        print('MY REPORT')
        print('-' * 50)
        f(text)
        print('-' * 50)
        print('Report completed: {}.'.format(datetime.now()))
    return inner

def report(text):
    print(text)

report = format_report(report)

report('I have created my first decorator.')'''

# Create a decorator using special decorator syntax:

from datetime import datetime

def format_report(f):
    def inner(text):
        print('MY REPORT')
        print('-' * 50)
        f(text)
        print('-' * 50)
        print('Report completed: {}.'.format(datetime.now()))
    return inner

@format_report
def report(text):
    print(text)

report('I have created my second decorator.')