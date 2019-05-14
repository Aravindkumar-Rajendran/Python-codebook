#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#Taking the number of times of input
times = int(input())

tweets = []     #List for saving the tweets

tweets_username = []    #List for saving the user names in the tweets

while times:
    no_people = int(input())  #Getting number of number of inputs 
    lis = []   
    for i in range(0, no_people):
        lis.append(input())  
    tweets.append(lis)   

    times -= 1   
    
for i in range(0, len(tweets)):
    temp = []
    for j in range(0,len(tweets[i])):
        tem = tweets[i][j].split(" ",1) # split the username from the tweets
        temp.append(tem[0])
    tweets_username.append(temp)
        
users = []
for i in range(0,len(tweets_username)):
    user_count = {}
    for j in range(0,len(tweets_username[i])):
        if j not in tweets_username[i][0:j]: # counting the number of times the username repeats
            user_count[tweets_username[i][j]] = tweets_username[i].count(tweets_username[i][j])
    users.append(user_count)


for user_count in users:
    user = user_count

    user = dict(sorted(user.items())) # Use sorted in find the alphabetical order to rank the user name

    u = list(user.values())
    u_keys = list(user.keys())
    
    pos = []
    for i in range(0, len(u)):
        if max(u) is u[i]:
            pos.append(i)  # Getting the max count
            
    for i in pos:
        print(u_keys[i]," ",u[i])

