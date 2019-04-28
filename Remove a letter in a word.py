# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 18:55:39 2019

@author: Aravind
"""

#Ways to remove i’th character from string in Python


def main():
    st = str(input("Enter the string: "))
    i = int(input("Enter the i: "))
    Ans = st.replace(st[i-1],"")
    print(Ans)
    
if __name__ == "__main__":
    main()