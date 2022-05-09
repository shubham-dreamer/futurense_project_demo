import pandas

#my_input=[2,3,4,5]
# list_manipulation=my_input*2
# print(list_manipulation)
#my_dimension=pandas.DataFrame(my_input)
# print(my_dimension)
# print(type(my_dimension))
#sum_of_list=my_dimension.sum()

# if we want to addition row-wise i.e horizontally then use axis=1 inside sum function
#sum_of_list=my_dimension.sum(axis)

#print(sum_of_list)



# 2d-dimensional---------------

#data = [[1, 5, 10], [2, 6, 9], [3, 7, 8]]
#
# # Create the pandas DataFrame
#df = pandas.DataFrame(data)

#sum_of_list=df.sum(axis=1)
#print(sum_of_list)

# specifying column names
# df.columns = ['Col_1', 'Col_2', 'Col_3']
# print(df, "\n")

#transpose of dataframe
# df = df.transpose()
# print("Transpose of above dataframe is-\n", df)



# 2d-dimensional list with hetrogenous value---------

#data = [['shubham', 50,"cse"], ['akash', 95,"ece"], ['Lov', 70,"eee"]]

# Creating the pandas DataFrame
#df = pandas.DataFrame(data, index=["first row","second row","third row"],columns=['Name', 'Marks','Subject'])

#Notes: index=[""] - this is used to change the name by default index name which are 0th,1th,2th index and so on.

#print(df)


#my_input={"names":["dhoni","kholi","raina"],"team":["csk","rcb","csk"],"score":[236,199,320]}
#my_dimension=pandas.DataFrame(my_input,index=["a","b"])
#my_dimension=pandas.DataFrame(my_input,index=["a","b","c"])
#print(my_dimension)
#print("----------------------------")
#print(my_dimension.loc["a"])
#print(my_dimension.iloc[0,0])


#to convert into CSV file

#my_dimension.to_csv("my_file")

#data= my_dimension.groupby(["team"])
#print(data)
# print(data.get_group("csk"))
#print(data.get_group("csk").groups)


#FINDING MEAN USING GROUP BY FUNCTION:::::::::::::::


# data ={"runs":[1,2,3,4],"score":[90,20,25,36],"player":["dhoni","dhoni","kholi","rohit"]}
# df_data = pandas.DataFrame(data)
#mean_data=df_data.groupby(["score"]).mean() #not work
# mean_data=df_data.groupby(["player"])["runs"].mean()
#
#
#
# print(mean_data)


data=pandas.read_excel("datahockey.xlsx")
df_data=pandas.DataFrame(data)
# print(df_data.columns)
print(df_data.groupby(['Country']))
print(df_data.groupby("Country")["Age"].mean().sort_values())

