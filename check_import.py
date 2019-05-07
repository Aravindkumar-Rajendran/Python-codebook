import palindrome

def main():
    Word = str(input("Enter the string: "))
    if palindrome.palindrome(Word):
        print ("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
