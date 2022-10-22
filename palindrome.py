import re
def is_palindrome(word):
    forward = ''.join(re.findall(r'[a-z]+', word.lower()))
    backward = forward[::-1]
    return forward == backward
