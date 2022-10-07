import secrets
import string

alpha = string.ascii_letters
digit = string.digits
collection = alpha + digit



def alphabet_pass(len):
    alpha_res = ''
    for i in range(len):
        alpha_res += ''.join(secrets.choice(alpha))
    return alpha_res


def digit_pass(leng):
    digit_res = ''
    for i in range(leng):
        digit_res += ''.join(secrets.choice(digit))
    return digit_res


def mixed_pass(len):
    mixed_res = ''
    for i in range(len):
        mixed_res += ''.join(secrets.choice(collection))
    return mixed_res


print(mixed_pass(7))