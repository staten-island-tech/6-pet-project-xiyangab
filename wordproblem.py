#Their email address
# Their password
# Before creating the new account, the function must verify that the email and password follow school rules:
# The email must be a string and must contain an "@" symbol.
# The password must also be a string.
# The password must be at least 8 characters long.
# The password must include at least one number.
# The password must include at least one uppercase letter.
# If ANY of these rules are broken, the function should return an error message explaining what went wrong.
# If EVERYTHING is good, the function should return a dictionary that represents the newly created user.

def valid(email, password):
    if type(email) != str or type(password) != str:
        return "email and or password must be a string"
    if "@" not in email:
        return "you need to have @"
    if len(password) < 8:
        return("you need at least 8 characters")
    if password.isdigit() == False:
        return "you need a number"
    if password.isupper() == False:
        return "you need an uppercase letter"
    
    return {'email': email, 'password': password}
print(valid("aa@", "FFFFFFFF"))

""" def has_numbers_any(inputString):
    return any(char.isdigit() for char in inputString)

# Example usage
string1 = "Hello123World"
string2 = "HelloWorld"
print(f"'{string1}' contains numbers: {has_numbers_any(string1)}")
print(f"'{string2}' contains numbers: {has_numbers_any(string2)}") """