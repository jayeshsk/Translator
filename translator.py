from langdetect import detect
import goslate

sentence = input("Enter data:")

word = sentence.split()
gs = goslate.Goslate()

for letter in word[0:]:

    print(letter +'=' + detect(letter))
    print(gs.translate(letter, 'en'))

