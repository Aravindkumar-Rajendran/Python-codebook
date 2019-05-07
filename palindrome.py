#Python program to check if a string is palindrome or not
def palindrome(inp):
    inp=inp.lower() #Lowering the case of the input
    rev = inp[::-1] #Using extended slicing to reverse the string
    if (inp==rev):
        return True
    return False

if __name__ == "check_import":
    print ("palindrome")