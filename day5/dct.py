mydict = {'pratik':1995,'biman':1998,'jayram':1997}
#find birthdate of pratik
print(mydict['pratik'])
#Add new element in mydict
mydict['kabita']=1993
print(mydict)
#get list of keys and values
print(mydict.keys())
print(mydict.values())
#get all elements of dictionary mydict as a tuples in list

print(mydict.items())
#check if year is in phone
phone ={
    'brand':'samsung',
    'model':'s22',
    'year':2022
}
if 'year' in phone:
    print("yes,year is in phone")
#update year with 2025
phone.update({'year':2025})
print(phone)

#to extract specific key value
#also del is used to delete certain value with key
phone.pop("brand")
print(phone)

#loop through both key and values
for x,y in phone.items():
    print(x,y)

#copy the dictionay in new sphone
sphone = phone.copy()
print(sphone)
company = {
    'ceo':'jayram',
'estd':1980,
}
#concatenate dictionaries phone and company using update

phone.update(company)
print(phone)


# Python code to merge dict using a single
# expression
def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res


# Driver code
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
dict3 = Merge(dict1, dict2)
print(dict3)

#nested dictionary
biman = {
    'address':'mangalbajar',
    'phone':9843552627,
    'college':'vedas'
}
pratik = {
    'address':'chabahil',
    'phone':982347762,
    'college':'himalaya'
}
interns ={
    'biman':biman,'pratik':pratik
}
#display dictionary as list
# print(interns.items())
# print(interns.values())
print(interns.get('biman'))
