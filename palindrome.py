#Python program to check if a string is palindrome or not
def palindrome(inp):
    inp=inp.lower() #Lowering the case of the input
    rev = inp[::-1] #Using extended slicing to reverse the string
    if (inp==rev):
        return True
    return False

def main():
    Word = str(input("Enter the string: "))
    if palindrome(Word):
        print ("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
