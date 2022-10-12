#Matrix - describe multi dim list, used in ML
a = [[1,23,2,3,34,1],[23,24,43,23,22],[23,23,123]]
print(a[1][2])
#list functions - append,insert,remove,pop(also for removing),clear (removes all in the list)

#when to usse what data struc. 
'''
dict has no oreder but list has 
if want data in order use list
if not use dict- has more info that a list'''

#dict keys should be always immutable,unique
#dict methods - to access keys use .get method
dictname = {
    'name': 'Karthik',
    'Status': 'Single',
    'class': 'tenth'
}
print(dictname.get('Status'))
#if key is not exist to set default val for the same
dictnamine = {
    'name': 'Karthik',
    'Status': 'Single',
    'class': 'tenth'
}
print(dictnamine.get('age', 34))
#check what it returns if key exists
dictnamine2 = {
    'name': 'Karthik',
    'Status': 'Single',
    'class': 'tenth',
    'age': 233
}
print(dictnamine2.get('age', 34))
#crete user with key val pairs!
userdictname = dict(name='Kinder')
print(userdictname)
#how to look for an item in a dict we use "in"
print("class" in dictnamine2)
#for check in keys use xxxxx.keys for values use xxxxx.values
print('age' in dictnamine2.keys())
print('tenth' in dictnamine2.values())
#for items key+val of 1 whole item
print(dictnamine2.items())