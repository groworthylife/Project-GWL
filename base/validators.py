from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re

SpecialSym =['$', '@', '#', '%', '!', '&', '^', '-', '_', '=', '+' ]


def validate_email(s):
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.match(pat,s):
        return s
    else:
        raise ValidationError(_("Invalid Email ID"), code=404)


def validate_pw(pw):
    res = True
    if len(pw) < 8:
        res = False
        raise ValidationError(_("Password length should be at least 8 characters"), code=404)
    if not any(char.isdigit() for char in pw):
        res = False
        raise ValidationError("Password should contain atleast one number", code=404)
    if not any(char.isupper() for char in pw):
        res = False
        raise ValidationError("Password should contain at least one uppercase character", code=404)
    if not any(char.islower() for char in pw):
        print('Password should have at least one lowercase letter')
        res = False
        raise ValidationError("Password should contain at least one lowercase character", code=404)
    if not any(char in SpecialSym for char in pw):
        res = False
        raise ValidationError("Password should contain at least one special character", code=404)
    if res:
        return res


def validate_name(pw):
    res = True
    if any(char.isdigit() for char in pw):
        res = False
        raise ValidationError("Name should not contain numbers", code=404)
    if any(char in SpecialSym for char in pw):
        res = False
        raise ValidationError("Name should not contain special characters", code=404)
    if res:
        return res


def validate_phone_no(s):
    Pattern = re.compile("(0|91)?[6-9][0-9]{9}")
    if Pattern.match(s) == None:
        raise ValidationError("Invalid Phone Number", code=404)
    else:
        return s

