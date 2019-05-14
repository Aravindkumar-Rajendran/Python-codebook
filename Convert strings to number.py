#!/usr/bin/env python
# coding: utf-8



def convert(text):
    ans = str("")
    for i in text:
        if (re.search(r'[A-Z]', i)) or (re.search(r'[a-z]', i)):
            ans += str(ord(i))
        else:
            ans +=i
        
    return ans




import re

test = 'sdrw12csdfd3ff45'
ans = convert(test)
print(ans)
print(type(ans))
ans = int(ans)
print(ans)
print(type(ans))

