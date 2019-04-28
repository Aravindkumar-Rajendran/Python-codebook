# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 19:21:23 2019

@author: Aravind
"""

# Python program to remove any special character 
  
# import required package 
import re 
  
# Function removes special character 
def run(string): 
  
    # Make own character set and pass  
    # this as argument in compile method 
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]') 
          
    outst = re.sub(regex,"",string) #replace the special character with Null
    print (outst)
      
  
def main():
    string = str(input("Enter a string:"))
    #string = "dshwiu%dmsm" 
    # calling run function  
    run(string)
    
if __name__ == "__main__":
    main()