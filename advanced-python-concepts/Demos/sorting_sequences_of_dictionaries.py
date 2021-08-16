from datetime import date
ww2_leaders = []
ww2_leaders.append({'fname':'Winston', 'lname':'Churchill', 
    'dob':date(1889,4,20)})
ww2_leaders.append({'fname':'Charles', 'lname':'de Gaulle', 
    'dob':date(1883,7,29)})
ww2_leaders.append({'fname':'Adolph', 'lname':'Hitler', 
    'dob':date(1890,11,22)})
ww2_leaders.append({'fname':'Benito', 'lname':'Mussolini', 
    'dob':date(1882,1,30)})
ww2_leaders.append({'fname':'Franklin', 'lname':'Roosevelt', 
    'dob':date(1884,12,30)})
ww2_leaders.append({'fname':'Joseph', 'lname':'Stalin', 
    'dob':date(1878,12,18)})
ww2_leaders.append({'fname':'Hideki', 'lname':'Tojo', 
    'dob':date(1874,11,30)})

ww2_leaders.sort(key=lambda leader: leader['dob'])
print('Leaders sorted by date of birth', ww2_leaders, '-'*70, sep='\n')

ww2_leaders.sort(key=lambda leader: (leader['lname'], leader['fname']) )
print('Leaders sorted by last name, first name', ww2_leaders, '-'*70, sep='\n')

from operator import itemgetter
ww2_leaders.sort(key=itemgetter('lname','fname'))
print('Leaders sorted by last name, first name using itemgetter', ww2_leaders, '-'*70, sep='\n')