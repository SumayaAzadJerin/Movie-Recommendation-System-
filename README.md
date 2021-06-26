# Movie-Recommendation-System-
Artificial Intelligence Project using Python
## A. PROJECT SUMMARY

**Project Title**:**Movie-Recommendation-System**

**Team Members:** 

<img width="622" alt="github" src="https://user-images.githubusercontent.com/82071078/123513674-e6d95600-d6c0-11eb-9906-23ab082f08ad.PNG">


- Sumaya Azad Jerin(B031920511)
- Aida Syafawati Binti Abdullah(B031910304)
- Nur Fairuza Syahira Binti Nor Hidan(B031910233)
- Nur Fajar Adillah (B031910373)



- [ ] **Objectives:**
- Help the user to search english movies based on their interest.
- To identify most relavent movies for each users within short time.
- To avoid unnecessaries movies.



##  B. ABSTRACT 

Nowadays we live in era of abundance. For any given product, there are many of options to choose from. For example like streaming videos, social networking, online shopping; the list goes on. Recommender systems help to personalize a platform and help the user find something they like. The easiest and simplest way to do this is to recommend the  items. However, to really enhance the user experience through personalized recommendations, we need dedicated recommender systems.There are several types of recommendation such as collaborative based filtering,content based filtering,hybrid filtering. Therefore, our group develop the content based recommendation movie engine for the english movie. The movie contains various of genres such as action, romantic, comedy, horor, documentation and etc. This recommendation based on attribute of movies 




![template](https://user-images.githubusercontent.com/82071078/123038802-a5784a80-d423-11eb-9da7-26e2d5bcdadc.jpg)

*The figure shows the flow for the Movie Recommendation system.*

From the figure, we can see when user watch or rate a movie, the system will generate or display the similar movie for the user to watch. The recommendation maybe from the same genres or cast from the previous movie.





## C.  DATASET
For this project, we use movie dataset that we get from the internet. This dataset contain 4810 of english movie details. We use three columns from the data which is genres, cast and keyword. Genres and cast data is important to make use the recommendation is related.


![Coding](https://github.com/SumayaAzadJerin/Movie-Recommendation-System-/blob/main/SAVE_20210625_111141.jpg)

*The figure shows three column sample of the dataset.* 


We choose this three column because when someone watch the movie he or she want to know and watch the other movie that the same cast acting. From that the recommendation is helpful for the user.

This is content based filtering recommendation system, we make this using cosine similarity which is a metric, helpful in determining, how similar the data objects are irrespective of their size. We can measure the similarity between two sentences in Python using Cosine it. In cosine similarity, data objects in a dataset are treated as a vector. The formula to find the cosine similarity between two vectors is –


Cos(x, y) = x . y / ||x|| * ||y||

where

x . y = product (dot) of the vectors ‘x’ and ‘y’.


||x|| and ||y|| = length of the two vectors ‘x’ and ‘y’.


||x|| * ||y|| = cross product of the two vectors ‘x’ and ‘y’.


so we make our dataset column into matrix using counterVector matrix and put this into cosine similairy for getting our expected data


<img width="551" alt="co" src="https://user-images.githubusercontent.com/82071078/123380391-f756d700-d5c1-11eb-8a81-4f521c961446.PNG">

*This figure shows code in python*




<img width="555" alt="gh" src="https://user-images.githubusercontent.com/82071078/123380795-777d3c80-d5c2-11eb-9e1f-398a4382e8b8.PNG">

*This figure shows how the engine sort similar movies*


we use scikitlearn for testing,training and plotting our dataset,we used these column from dataset fro train,test,and plot

![moviedata](https://user-images.githubusercontent.com/82071078/123382078-19515900-d5c4-11eb-9832-d70488d225c7.PNG)




We have split  80% for testing and 20% for training these column of dataset



<img width="638" alt="split" src="https://user-images.githubusercontent.com/82071078/123382992-2e7ab780-d5c5-11eb-8d41-c674a401cf1f.PNG">

*This figure shows splitting column dataset*





![image](https://user-images.githubusercontent.com/82071078/123383739-1bb4b280-d5c6-11eb-9c7d-9e0a9dd2e489.png)

*This figure shows code for plotting*



<img width="441" alt="plot" src="https://user-images.githubusercontent.com/82071078/123381196-fd00ec80-d5c2-11eb-81e0-b6380e4c6cd9.PNG">

*This graph shows the accuracy* 

We can see the accuracy of our dataset from plotting.

## D.   PROJECT STRUCTURE

The following directory is our structure of our project:

$ tree --dirsfirst --filelimit 8

- ├── Output 2.png
- ├── SourceCode.py
- ├── Testing Dataset.py
- ├── movie_dataset.csv
- ├── output 1.png
- ├── plot.png
- ├── SAVE_20210625_111141.jpg
- ├── moviedata.png

8 files

The dataset/ directory contains the data described in the “Movie Recommendation System Dataset” section.

Two images provided are the examples of the engine of movie recommended which is output 1 and output 2.








## E.  RESULT AND CONCLUSION



Nowadays, recommendation system is popular on various platform like Netflix,Amamzon, facebook and so on.This project is used to build movie recommendation system using python in machine learning environment. This is content based recommendation system where the system will take data from user, either user will click movie or rate any movie, so the system will save the information on its database and  suggest user the similar content. If user put more input the system will be more accurate.

 You can search any movie that you want to watch and the system will provide 10 recommendation list of movies that related with.Here are our output:





![New Project (1)](https://user-images.githubusercontent.com/82071078/123362928-16df0700-d5a4-11eb-9dd0-d50eb7820762.jpg)

*The figure shows 10 recommendation movies that related with ***Avatar***.* 


![New Project](https://user-images.githubusercontent.com/82071078/123363041-51e13a80-d5a4-11eb-815d-c258206f41d9.jpg)

*The figure shows 10 recommendation movies that related with ***Titanic***.*



## F.   PROJECT PRESENTATION 

[![Movie Recommendation System](https://img.youtube.com/vi/azgyUE408Ck/0.jpg)](https://www.youtube.com/watch?v=azgyUE408Ck "Movie Recommendation system")



##  G. Acknowledgement
We refer these websites for building Our project
- https://www.codeheroku.com/
- https://medium.com/@cyberwillis/epoch-training-validation-testing-sets-whats-all-this-means-61d501a42497
- https://www.w3schools.com/python/python_ml_train_test.asp

