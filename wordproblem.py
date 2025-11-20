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
""" 
def valid(email, password):
    if type(email) != str or type(password) != str:
        return "email and or password must be a string"
    if "@" not in email:
        return "you need to have @"
    if len(password) < 8:
        return("you need at least 8 characters")
    if not any(char.isdigit() for char in password):
        return "you need a number"
    if not any(char.isupper() for char in password):
        return "you need an uppercase letter"
    return {'email': email, 'password': password}
print(valid("aa@", "FFFFFFFF345345"))
 """

password = 'jaja   jajaja  jajajaja '
print(password.strip())