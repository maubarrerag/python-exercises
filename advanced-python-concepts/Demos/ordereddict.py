from collections import OrderedDict

car_conditions=OrderedDict()

car_conditions['E']='Excellent'
car_conditions['G']='Good'
car_conditions['F']='Fair'
car_conditions['P']='Poor'

print('The ordered dictionary condition keys and values:')
for (key, value) in car_conditions.items():
    print('Condition key: ' + key + ' condition value: ' + value)
print('-'*70)    

# define a function to sort by value:
def sort_by_value(ccd):
    return ccd[1]

# create dictionary in car condition value order 
# using named function:
car_conditions_value=OrderedDict(sorted(car_conditions.items(),
    key=sort_by_value))
print('''The value ordered dictionary condition keys 
	and values using named function:''')
for (key, value) in car_conditions_value.items():
    print('Condition key: ' + key + ' condition value: ' + value)
print('-'*70)

# create dictionary in car condition value order 
# using lambda function:
car_conditions_value=OrderedDict(sorted(car_conditions.items(),
    key=lambda ccd: ccd[1]))
print('''The value ordered dictionary condition keys 
	and values using lambda function:''')
for (key, value) in car_conditions_value.items():
    print('Condition key: ' + key + ' condition value: ' + value)
print('-'*70)