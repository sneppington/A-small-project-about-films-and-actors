vHello<br>
This project uses the following database <br> 
https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows<br><br> 


I wanted to use this database to find out which one were the actors that had made the most films of each genre, <br> 
and which one of them is the one who produces the most money per film on average<br> <br> 

The first step to do this was to get a list of all the actors,<br>
each row has got 5 columns, each one containing one of the actors who appeared,<br>
and some actors appeared more than once.<br>

So I wrote this Python program.<br>
![image](https://github.com/sneppington/wa/assets/140338265/41e1393b-907c-40cb-a0fb-1bf69b1ed524)<br><br>
This program iterates through all the rows of the database(I named it x),<br>
if it detects that the name of that actor already is inside of the actors table, it doesn't insert it, but if it isn't, it inserts it.<br>
There also is another function called insert_zeros(), which has to do with something in advance.<br><br>

After that, I got this list<br>
![image](https://github.com/sneppington/wa/assets/140338265/eb1c6254-4181-49c2-85e6-12c358332bbc)<br>
It is much longer.<br><br>


The next step was to get a list of all the genres
