days = {'sunday','monday','tuesday','wednesday'}
newdays = days
print(newdays)
#delete set completely
del newdays
#add thursday to set
days.add('thursday')
print(days)

newset = {4,5,2,7,1}
print(newset)
days1 = {'friday','saturday'}
#union of sets
days3 = days.union(days1)
print(days3)
#intersection of sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z=x.intersection(y)

print(z)
