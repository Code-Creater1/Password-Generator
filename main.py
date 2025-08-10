import string
import random

if __name__ == "__main__":
    # Character sets
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    #s4 = string.punctuation 

    # Take valid input from user
    user_input = input("Enter password length: ")

    if user_input.isdigit():
        password_length = int(user_input)

        if password_length < 4:
            print("Password should be at least 4 characters long.")
        else:
            # Combine all selected character sets
            s = []
            s.extend(list(s1))
            s.extend(list(s2))
            s.extend(list(s3))
            #s.extend(list(s4))  
            
            print("Your password length is:", password_length)
            print("Your password is:")
            print("".join(random.sample(s, password_length)))
    else:
        print("Invalid input! Please enter a number.")
