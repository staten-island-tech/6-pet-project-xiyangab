def valid(email, password):
    email.strip()
    password.strip()
    if "@" not in email:
        return "you need to have @"
    elif len(password) < 8:
            return("you need at least 8 characters")
    elif int not in password:
         return "you need a number"
    elif password.isupper() == False:
         return "you need an uppercase letter"
valid("afafafafaf", "jajajajaja")