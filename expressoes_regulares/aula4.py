import re

string ='''
What is Lorem Ipsum?
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was lorem popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
Aorem 
aorem
poRem joooooooooãooooooooo
porem
'''

print(re.findall(r'jo+ão+', string, flags=re.I))
print(re.findall(r'jo{1,}+ão{1,3}+', string, flags=re.I))
# print(re.sub(r'jo+ão+','Agosto', string, flags=re.I))