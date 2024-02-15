import re

def password_strength(password):

    if len(password) < 8:
        return "Very weak: Password must be at least characters long."
    elif len(password) >= 16:
        strength = 1
    else:
        strength = 0.5


    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        strength += 0.5
    else:
        return "Weak: Password must contain both uppercase and lowercase letters."


    if re.search(r'\d', password):
        strength += 0.5
    else:
        return "Weak: Password must contain at least one number."


    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 0.5
    else:
        return "Weak: Password must contain at least one special character."


    if strength == 1:
        return "Strong: Good job!"
    elif strength == 1.5:
        return "Medium: Consider adding more complexity to your password."
    else:
        return "Very weak: Please improve your password by following the recommendations."


password = input("Enter your password: ")
print(password_strength(password))




