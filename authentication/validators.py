import re

SpecialSym =['$', '@', '#', '%', '!', '&', '^', '-', '_', '=', '+' ]

ValidStanderds = ["8th", "9th", "10th", "11th", "12th"]


def validate_standerd(st):
    if st not in ValidStanderds:
        return False
    return True

def validate_age(a):
    if a<10 or a>100:
        return False
    return True


def validate_email(s):
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.match(pat,s):
        return True
    return False


def validate_pw(pw):
    if len(pw) < 8:
        return False
    if not any(char.isdigit() for char in pw):
        return False
    if not any(char.isupper() for char in pw):
        return False
    if not any(char.islower() for char in pw):
        print('Password should have at least one lowercase letter')
        return False
    if not any(char in SpecialSym for char in pw):
        return False
    return True


def validate_name(pw):
    if any(char.isdigit() for char in pw):
        return False
    if any(char in SpecialSym for char in pw):
        return False
    return True


def validate_phone_no(s):
    Pattern = re.compile(r"^\d{10}$")
    if Pattern.match(s) == None:
        return False
    return True

