# -*- coding: utf-8 -*-
import pandas as pd

print("wagoo")


x = pd.read_csv("D:\SQLite.csv")

Genre_list = []

last_word_pos = 0





for index, row in x.iterrows():
    
    
    last_word_pos = 0
    
    for i in range(0, len(row['Genre'])):
        if row['Genre'][i] == ",":
            
            
            print(row['Genre'][last_word_pos:i])
            
            
            if row['Genre'][last_word_pos:i] not in Genre_list:
                Genre_list.insert(0,row['Genre'][last_word_pos:i])
            
            
            
            if row['Genre'][i+1] == " ":
                last_word_pos = i+2
            else:
                last_word_pos = i+1
        
            
            
            
        





print(Genre_list)




