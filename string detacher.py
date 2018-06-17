import re

sentence=input("Enter para:")
words=re.sub("[/w]"," ",sentence).split()
print(words)
