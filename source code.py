#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import libraries
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#load csv files
df=pd.read_csv(r'C:\Users\jerin\OneDrive\Desktop\AI_BITI1113\Malay_Movie_Dataset.csv',encoding='ANSI') 

df.head()

#select attirbutes
attributes = ['Director','Cast','Genre']



#create function for combining values 
def combine_attributes(row): 
    return row['Director']+" "+row['Cast']+" "+row['Genre']



#fill NAN with blank string
for attribute in attributes:
    df[attribute] = df[attribute].fillna('') 
    
#stroing attributes vertically
df["combine_attributes"] = df.apply(combine_attributes,axis=1)

#select sinlge row from dataframe
df.iloc[0].combine_attributes



#create obj
obj = CountVectorizer() 

#stroing attributes into CountVectorizer() obj
count_matrix = obj.fit_transform(df["combine_attributes"]) 

#get cosine similarity
cosine_similar = cosine_similarity(count_matrix)



#get index from movie title
def index_from_Title(Title):
    return df[df.Title == Title]["index"].values[0]

user_likes_movie = "Sini Ada Hantu"

movie_index = index_from_Title(user_likes_movie)
similar_movies = list(enumerate(cosine_similar[movie_index]))


sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)[1:]

#get movie title from index
def Title_from_index(index):
    return df[df.index == index]["Title"].values[0]

i=0
print("Best 10 movies similar to "+user_likes_movie+" are:\n")

for movie in sorted_similar_movies:
    print(Title_from_index(movie[0]))
    i=i+1
    if i>10:
        break

