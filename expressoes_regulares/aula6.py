import re

text = """
    <p>exemplo de paragrafo</p> <div>exemplo de div</div>
    <p>exemplo de paragrafo2</p>
"""

print(re.findall(r'<([divp]{1,3})>.*<\/\1>', text))
print(re.findall(r'<[divp]{1,3}>.*?<[\/dpiv]{1,3}>', text))
# corrigir