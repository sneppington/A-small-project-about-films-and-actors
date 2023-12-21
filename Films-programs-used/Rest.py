# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 06:59:23 2023

@author: osama
"""

import pandas as pd



genres = ['War', 'Film-Noir', 'Sci-Fi', 'History', 'Music', 'Musical', 'Fantasy', 'Thriller', 'Romance', 'Horror', 'Mystery', 'Family', 'Animation', 'Comedy', 'Drama', 'Biography', 'Adventure', 'Action', 'Crime','Western']

Genre_list=[]


actors = {
    
    "name":[],
    'War':[],
    'Film-Noir':[],
    'Sci-Fi':[],
    'History':[],
    'Music':[],
    'Musical':[],
    'Fantasy':[],
    'Thriller':[],
    'Romance':[],
    'Horror':[],
    'Mystery':[],
    'Family':[],
    'Animation':[],
    'Comedy':[],
    'Drama':[],
    'Biography':[],
    'Adventure':[],
    'Action':[],
    'Crime':[],
    'Western':[],
    'Sport':[],
    'Films':[],
    'Produced':[]
    
     
}
    
x = pd.read_csv("D:\movypdt.csv")


def insert_zeros():
    for i in actors:
            if i != "name":
                actors[i].insert(0,0)
    









for i,v in x.iterrows():
    
    
    
    
    
    
    if v["Star1"] not in actors["name"]:
         actors["name"].insert(0,v["Star1"])
         insert_zeros()
    if v["Star2"] not in actors["name"]:
        actors["name"].insert(0,v["Star2"])
        insert_zeros()
    if v["Star3"] not in actors["name"]:
       actors["name"].insert(0,v["Star3"])
       insert_zeros()
    if v["Star4"] not in actors["name"]:
        actors["name"].insert(0,v["Star4"])
        insert_zeros()
    

        
    
    







def counter(row,numb:int):
    inx=actors["name"].index(row['Star'+str(numb)])
    
    
    
    actors["Films"][inx]+=1
    
    gross = 0
    if isinstance(row["Gross"],str):
        for i in row["Gross"]:
            print(i)
            if i != ",":
                gross = int(gross * 10 + int(i))
    elif isinstance(row["Gross"],int):
        gross = int(row["Gross"])
    else:
        gross = 0
    print(gross)
    actors["Produced"][inx]+=gross
    
    
    for i in Genre_list:
        actors[i][inx] += 1
    
    
    
    
    
    














for index, row in x.iterrows():
    
    
    last_word_pos = 0
    
    for i in range(0, len(row['Genre'])):
        print(i == len(row['Genre'])-1, i, len(row['Genre'])-1)
        
        if row['Genre'][i] == ",":
            
            
            
            
            if row['Genre'][last_word_pos:i] not in Genre_list:
                Genre_list.insert(0,row['Genre'][last_word_pos:i])
            
            
            
            if row['Genre'][i+1] == " ":
                
                last_word_pos = i+2
            else:
                last_word_pos = i+1
    
        if i == len(row['Genre'])-1:
            
            if row['Genre'][last_word_pos:i] not in Genre_list:
                Genre_list.insert(0,row['Genre'][last_word_pos:i+1])
            
            
        
    if row["Series_Title"] == "The Shawshank Redemption":
        print(row["Star3"])
        print(row["Genre"])

    counter(row,1)
    counter(row,2)
    counter(row,3)
    counter(row,4)
    
    
    
    
    
    
    Genre_list.clear()
    
    
    
    
print(pd.DataFrame(actors))

pd.DataFrame(actors).to_csv("Actors_with_numbers_new_one.csv")









