import re
def name_validation(name):
    name_pattern = r"[a-zA-z]+"
    return  bool(re.fullmatch(name_pattern , name.strip())) and bool(len(name)>=3)

def email_validation(email):
    email_pattern = r"[a-zA-Z0-9._%+-]+@gmail\.com"
    return bool(re.fullmatch(email_pattern , email.strip()))