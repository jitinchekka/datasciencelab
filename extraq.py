#  Use the ratings given by users to recommend movies. Implement the following menus,
# Count Users
# Count Movies
# Display User Information
# Display Movie Name
# Recommend Movie
# Import Dataset.csv and Movie_Id_Titles.csv
# Create a dictionary of movie id and title
import pandas as pd
df=pd.read_csv('Dataset.csv')
#convert dataframe to dictionary
data_dict={}
for i in range(len(df)):
    data_dict[df['user_id'][i]]=df['item_id'][i]   
print(data_dict)
df2=pd.read_csv('Movie_Id_Titles.csv')
print(df)
# print(df2)
data_dict_2={}
for i in range(len(df2)):
    data_dict_2[df2['item_id'][i]]=df2['title'][i]
# print(data_dict_2)