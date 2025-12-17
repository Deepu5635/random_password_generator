import random
import string

def generate_password(length):
    # Combine all possible characters: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly pick characters from the list 'length' times
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# --- Main Program ---
print("Welcome to the Python Password Generator!")

# Get user input for password length
size = int(input("How many characters should the password be? "))

# Generate and print the result
new_password = generate_password(size)
print(f"Your new password is: {new_password}")