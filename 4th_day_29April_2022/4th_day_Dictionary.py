# var={"name":"shubham"}
# print(var)
# print(type(var))

# var={"name":"shubham","name":"kholi"}
# print(var)
# print(type(var))


# you can't add two dictionary using + operator because + operator works on indexes.
# var={"name":"dhoni"}
# var1={"age":33}
# print(var + var1)

#Dictionary belongs to mutable category
#concatenate dictionary:
#1st method:
# var={"name":"dhoni"}
# var1={"captain":"msd"}
# o={**var,**var1}
# print(o)


#2nd method:
# var={"name":"shubh"}
# var1={"captain":"keeper"}
# var.update(var1)
# print(var)
# print(dir(var))

#Any imutable reseved words can be used as keys,like:int

# var={1:"dhoni",True:"kholi",1.0:"rohit"}
# print(var[1])

# var={"name":"dhoni",True:"kholi",3:"raina",5.9:"ashwin",{"a","b"}:"kartik"}
# print(var)
# print(type(var))

# var={"name":"dhoni"}
# print(dir(var))
#
# var={"name":"dhoni"}
# var["country"]="india"
# print(var)
#
# var{"name":"dhoni"}
# var["name"]="kholi"
# print(var)


#sorting Dictionary on basis of keys:

# var={"name":"dhoni","age":34,"team":"csk","born_year":1999}

# for i in sorted(var.keys()):
#     print(i, end=" ")


#sorting keys and returning dictionary:
# output=dict(sorted(var.items()))
# print(output)


# keys=[]
# for x in var.keys():
#     keys.append(x)
# print(keys)


# sorted_keys=sorted(keys)
# print(sorted_keys)

# sorted_dict={}
# for x in sorted_keys:
#     sorted_dict[x] = var[x]
# print(sorted_dict)


#dictionary Comprehension:
# sorted_dict= {x:var[x] for x in sorted([x for x in var.keys()])}
# print(sorted_dict)


#Sorted vs Sort
var1=["dhoni","ashwin","sachi","raina"]
# var1.sort()
# print(var1)

# print(sorted(var1,reverse=True,key=len),var1)


#Give single Quotes internally when Double Quotes are there externally i.e is making it as string

import json

#var="{'name':'shubham','age':22}"
#print(var)
# print(type(var))


var='{"name":"shubham","age":22}'
#for converting to dictionary from String
# var_dict=json.loads(var)
# print(var_dict)
# print(type(var_dict))

#conversion from dictionary to String
# var_string=json.dumps(var_dict)
# print(var_string)
# print(type(var_string))


#Pop

#in List pop function can be used without any arguments and it throws last item
# var=["a","b","c"]
# var.pop()
# print(var)


# When pop is used in dictionary we must pass argument i.e. key which data we want to throw
# var={"name":"shubham","age":33,"team":"csk"}
# var.pop("age")
# print(var)


#In dictionary, popitem we can use without giving any argument and
# it will throw last item of the dictionay(key and value both)
# var.popitem()
# print(var)

#STRING MANIPULATION------

# str="shuBham"
# print(str.encode())
# print(str.capitalize()) #make only first character of string capital
# print(str.casefold())  #make whole string in lower case
# print(str.center(20))  #require  1 argument, then upto that place it gives spaces upto that numberof places
#
#
# str1="this is a ice-cream"
# print(str1.count("ice")) #take character/ word as argument and tells how many times it occurs
#
# print(str.endswith("a")) #return True if it end with that particular letter/character.

#Sorting Object----------

class stud:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def show(self):
        print(self.name,self.roll)
k=[]
obj1=stud("shubham",1)
k.append(obj1)

obj2=stud("dhoni",2)
obj3=stud("kholi",3)
obj4=stud("raina",4)
obj5=stud("bumrah",5)
obj6=stud("jadeja",6)
k.append(obj2)
k.append(obj3)
k.append(obj4)
k.append(obj5)
k.append(obj6)

k.sort(key=lambda stud:(stud.roll,stud.name))
print(k)
#print(obj2.name)








