#STRING BASICS

# var ="dhoni"
# var1="kholi"
# var,var1=var1,var
# print(var)
# print(var1)

# var="""dhoni is best captain
# india ever witnessed"""
# print(var)

# var="dhoni is best captian\
# india ever witnessed"
# print(var)

# var =r"C:\newfolder\testing.txt"

#Shallow copy
# var=["delhi","patna","goa"]
# var1=var
# print(var)
# print(var1)
# var[1]="Rohit"
# print(var)


#deep copy
# var=["delhi","asssam","punjab"]
# var1 = var[:]
# print(var)
# print(var1)
# var1[1]="Rohit"
# print(var)
# print(var1)

#deep copy using copy i.e. inbuilt function:
# var=["hp","lenovo","dell"]
# var1= var.copy()
# print(var)
# print(var1)
# var1[1]="Predator"
# print(var)
# print(var1)

#count Function: gives count of characters
var="India has rich history"
# print(var.count("i"))
# print(var.count("i",2))
# print(var.count("i",2,5))

#find function: give index of character occuring first
# var="India has rich history"
# print(var.find("i"))
# print(var.find("i",2))
# print(var.find("i",2,5))
# print(var.rfind("i"))

#index Function: also gives index of character occuring first but if character is not there it gives Error whereas find gives -1
# print(var.index("i"))
# print(var.index("i",2))

#split function:
# output=list(var)
# print(output)
# output = var.split()
# print(output)

# output1=var.split("i")
# print(output1)
#
# output2=var.split("i",2)
# print(output2)
#
# output3=var.partition("i")
# print(output3)

#Strip Function:

print(len(var))
output=var.strip()
print(output)
print(len(output))

var="!!India is!!"
output1=var.strip("!")
print(output1)

var="!india is in"
output3=var.strip("!i")
print(output3)

#Enumeration
# var=["a","b","c","d","e"]
# for x,y in enumerate(var[:]):
#     if x%2==0:
#         # var.pop(x)
#         var.remove(y)
# print(var)

# var=["a","b","c"]
# for x in range(0,len(var)):
#     data=var[x].upper()
#     var.append(data)
# print(var)
