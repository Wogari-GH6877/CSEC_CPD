#Word
word=(input())
capital=[]
small=[]
for letters in word:
    if letters==letters.upper():
        capital+=letters
    elif letters==letters.lower():
        small+=letters
num_capital=len(capital)
num_small=len(small)
if num_capital<num_small or num_capital==num_small:
    print(word.lower())
else:
    print(word.upper())
