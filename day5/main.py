#list example
mylist = ['hello','i','am','jay']
mytuple =('i','am','jayram')
myset = {'apple','mango','orange','banana'}
mydict = {'jayram':'raut','biman':'shrestha','pratik':'basnet'}
# print(my_dict)
# my_list.append(12)
# print(my_list[:4])
# my_list[2] = 'jayram'
# print(my_list)
# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)
#
# thislist[2:]=[123,45,6]
# print(thislist)
# mylist.insert(2,'z')
# print(mylist)
# thislist.extend(mylist)
# print(thislist)
# mylist.clear()
# print(mylist)
# mylist.sort(reverse = True)
# print(mylist)
#sorting with key
# newlist = [56,54,33,44,22,90]
# print(newlist)
# def func(n):
#     return abs(n-50)
#
# newlist.sort(key = func)
# # print(newlist)
# # ch = 'jayram'
# # print(ch.__reversed__())
# # print(ch.reverse())
# x = ['hello i am jay jay jay','hello i am pratik']
# x.reverse()
# print(x)
# if 'i' in mylist:
#     print(mylist)
#
# mylist[1:2]=["h","i"]
# print(mylist)
#
# newtuple = tuple(mylist)
# mylist.append("raut")
# ram = ("ram",)
# newtuple+=ram
# print(newtuple)
#access all values of tuple using variable
fruits = ("apple", "banana", "cherry","mango")

(green, *yellow, red) = fruits

print(green)
print(yellow)
print(red)

#multiply the content o f tuple
afruits=fruits*2
print(afruits.index("mango"))
print("apple" in afruits)


#list of set
mylist =[1,2,3]
set1={1,2,3,4}
set2={5,6,7}
listset = [set1,set2,mylist]
print(listset)