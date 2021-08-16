from collections import OrderedDict

order_status =  {'O': 'open', 'S': 'shipped', 'B': 'backordered',
    'X': 'cancelled', 'R': 'returned'}
   
def ordering (od):
    return od[0]

od_order_status = OrderedDict(sorted(order_status.items(), 
    key=lambda od: od[1]) )
print('''Ordered dictionary with lambda function 
	for ordering by value:''')
for (key, value) in od_order_status.items():
    print("key: " + key + " value: " + value)
print('-'*70) 

od_order_status = OrderedDict(sorted(order_status.items(), 
     key=ordering))
print('Ordered dictionary with named function for ordering by key:')
for (key, value) in od_order_status.items():
    print("key: " + key + " value: " + value)
print('-'*70)   

# add an order status:
od_order_status['D']='damaged'  
print('Ordered dictionary after adding an order status:')
for (key, value) in od_order_status.items():
    print("key: " + key + " value: " + value)
print('-'*70)  

# delete the last item ('D') :
od_order_status.popitem()
print('Ordered dictionary after popitem():')
for (key, value) in od_order_status.items():
    print("key: " + key + " value: " + value)
print('-'*70)