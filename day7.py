### hang man
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lists=["khang","hoang","thai"]
chosen=random.choice(lists)
l=len(chosen)
display=["_" for i in range(l)]
live=6
end=False
k=""
while end==False:
    guess=input("Guess a letter: ").lower()
    for j in range(l):
        letter = chosen[j]
        if guess==letter:
            display[j]=letter
    k=" ".join(display)
    print(k)
    print(stages[live])
    if guess not in chosen:
        live-=1
        if live==0:
            print("Lose")
            end=True
    if "_" not in display:
        print("Win")
        end=True