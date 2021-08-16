import datetime

def str_to_date(str_date):
    dates = str_date.split('-')
    dat = datetime.date(int(dates[0]), int(dates[1]), int(dates[2])) #asi lo hice
    parts = [int(part) for part in str_date.split('-')] #mas elegante
    return datetime.date(*parts)

str_date = input('Input date as YYYY-MM-DD: ')
dat = str_to_date(str_date)
print (dat)