# import the necessary module 
import random
import string

def generate_password(length=13):
    # Define the character sets to use in the password
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation
    
    # Combine all the character sets
    all_characters = lower + upper + digits + punctuation
    #comment 
    # Generate a random password using the combined character sets
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

# Example usage
password_length = 13
new_password = generate_password(password_length)
print(f"Generated password: {new_password}")
