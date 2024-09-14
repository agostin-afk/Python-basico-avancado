import re

string = "Esse é um teste de expressoes regulares"


print(re.search("teste", string))
print(re.findall("teste", string))
print(re.sub("teste","ABCD", string))
print(re.findall("teste", string))
print(string[10:15])

regex = re.compile("teste")
print(regex.search(string))