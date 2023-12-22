# -*- coding: utf-8 -*-
import pandas as pd



x = pd.read_csv("D:\SQLite.csv")

Genre_list = []

last_word_pos = 0


word = ""


for index, row in x.iterrows():
    
    
    last_word_pos = 0
    
    for i in row['Genre']:
        if i == ",":
            if word not in Genre_list:
                Genre_list.insert(0,word)
                
            word = ""
            
        if i != " " and i != ",":
            word = word + i
            
            
            
    if word not in Genre_list:
        Genre_list.insert(0,word)
        
        
    word = ""
            
            
            

        
            
            
            
        





print(Genre_list)




