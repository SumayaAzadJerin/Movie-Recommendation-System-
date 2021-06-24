#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
import matplotlib.pyplot as plt
from sklearn import linear_model



#load CSV
df=pd.read_csv(r'C:\Users\jerin\OneDrive\Desktop\AI_BITI1113\movie_dataset.csv') 


#split Data
X = np.asarray(df[['id', 'vote_average','popularity']])
Y = np.asarray(df['vote_count'])
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20, shuffle= True)



X_train.shape     
X_train.shape     


reg = linear_model.Ridge (alpha = .5)
reg.fit(X_train, y_train)
print('Score: ', reg.score(X_test, y_test))
print('Weights: ', reg.coef_)
plt.ylabel('Accuracy')
plt.plot(reg.predict(X_test))
plt.plot(y_test)
plt.show()


# In[ ]:




