```python
''' It's a python program to find a list of integers is a part of fibonacci series'''

#Function to Check the first number in Fibonacci sequence
def chkFib(n):
    a=0;b=1;c=a+b
    while (c<=n):
        if(n==c):
            return True
        a=b;b=c;c=a+b
    return False


#Function to check the list in a part of Fibonnaci series
def is_fibnocci(lst):
    lst.sort() # sorting the list
    Fibchk=0 # temporary variable to fibonacci check the first num in list

    if(lst[0]==0 or lst[0]==1):
        Fibchk=True
    else:
        Fibchk=chkFib(lst[0]) #Calling the nested function to fibancci check the first num

    if(Fibchk==True): 
        for i in range(0,(len(lst)-2)):#Checking the fibonacci order from the second number to the last
            if(lst[i]+lst[i+1] != lst[i+2]):
                    return False
        return True
    else:
        return False
    

#Enter the list of integers here
lst=[34, 21, 89, 55]
res = is_fibnocci(lst)
if(res==True):
    print ("Yes, the list is part of the fibonacci Sequence")
else:
    print("No, the list is not part of the fibonacci Sequence ")
```