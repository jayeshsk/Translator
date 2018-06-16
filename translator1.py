from langdetect import detect
import goslate

sentence=input("Enter data:")

for words in sentence:
print(detect(sentence))

gs=goslate.Goslate()
print(gs.translate(sentence,'en'))
