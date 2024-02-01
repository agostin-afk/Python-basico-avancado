import re

NUM_OR_DOT = re.compile(r'^[0-9.]$')
def NumOrDot(string:str) -> bool:
    return bool(NUM_OR_DOT.search(string))

def isValidNumber(string: str):
    valid = False
    try:
        float(string)
        valid = True
    except ValueError:
        valid = False
    return valid

