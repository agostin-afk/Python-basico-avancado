import re

NUM_OR_DOT = re.compile(r'^[0-9.]$')
def NumOrDot(string:str) -> bool:
    return bool(NUM_OR_DOT.search(string))

def NumTransform(string:str) -> (float | int):
    try:
        float(string)
    except ValueError as e:
        print(f"Erro de valor: {e}")  
    try:
        if float(string) == int(float(string)):
            return int(float(string))
        else:
            return float(string)
    except ValueError as e:
        return f'Erro 45: {e}'


def isValidNumber(string: str):
    valid = False
    try:
        float(string)
        valid = True
    except ValueError:
        valid = False
    return valid

