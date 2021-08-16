from collections import deque

todays_agenda=deque(['Staff meeting at 10AM',
    'Database upgrade late AM',
    'Accounts payable software test at 2PM',
    'System maintenance in the evening'])

items_added_start_of_day=['Conference call with London customer',
	'Brew a good pot of coffee!']
item_inserted='Accounts receivables unit test, late afternoon'
item_added_late_night='Restart servers'

print('Today\'s agenda:')
for agenda_item in todays_agenda:
    print(agenda_item)
print('-'*70)

# We have to add some items that are to occur prior to staff meeting:
todays_agenda.extendleft(items_added_start_of_day)

print('Today\'s agenda after appending early morning items:')
for agenda_item in todays_agenda:
    print(agenda_item)
print('-'*70)

# Remove Database upgrade... agenda item:
todays_agenda.remove('Database upgrade late AM')
print('Today\'s agenda after removing Database upgrade:')
for agenda_item in todays_agenda:
    print(agenda_item)
print('-'*70)

# Insert new agenda item at position 4 
# (immediately after Accounts payable software test):
todays_agenda.insert(4, item_inserted)
print('''Today\'s agenda after inserting new agenda item 
    Accounts receivable unit test... at position 4''')
print('''(Positions displayed below to affirm new item 
    is located at position 4):''')

for item_seq, agenda_item in enumerate(todays_agenda):
    print(str(item_seq) + ') ' + agenda_item)
print('-'*70)

# Add a final item to the end of the agenda (latest time):
todays_agenda.append(item_added_late_night)
print('''Today\'s agenda after inserting 
    new agenda item Restart servers''')
for agenda_item in todays_agenda:
    print(agenda_item)
print('-'*70)