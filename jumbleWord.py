import random
words=["programing","python","english","playgame","although","despite","inspiteof","eventhough"]
[t for t in words ]
word = random.choice(words)
guess="".join(random.sample(word,len(word)))
print(f"the jumble word is {guess}")
jumble=input("Nhap word:")
if jumble == word:
    print("Corect\n")
else :
    print(f"In correct Word:{word}\n")

