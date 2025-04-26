def palindrome(string):
#Remove any spaces and converts the string to lowercase
    string=string.replace(" ","").lower()
    #check if the string is equal to its reverse
    return string==string[::-1]
#example usage:
print(palindrome("madam"))
