#Take input from the user
char=input("Enter a single character:")
if len(char)!=1:
    print("Please enter only one character!")
else:
    #check if the character is a digit
    if char.isdigit():
        print(f"{char}'is a digit.")
    #check if the character is a lowercaseletter
    elif char.islower():
         print(f"'{char}'is a lowercase character.")
    #check if the character is an upper letter
    elif char.isupper():
         print(f"'{char}'is an uppercase character.")
    #if none of the above,it is a special character
    else:
         print(f"'{char}'is a special character.")
