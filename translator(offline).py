from langdetect import detect
import re

sentence=input("Enter data:")
words=re.sub("[^/w]",' ','sentence')

for x in words:
    print(x+"="+detect(x))
