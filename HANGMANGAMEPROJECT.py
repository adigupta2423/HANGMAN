import random

words=["apple","orange","attitude","battle","house","power","question","gratitude","kite","nose","world","sun","wonder","cute","cat","moment","player"]
stages=['''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |     
=========       
''',''' 
+---+
 |   |
 O   |
/|\  |
/    |
     |     
=========
''',''' 
+---+

 |   |
 O   |
/|\  |
     |
     |     
=========
''',''' 
+---+
 |   |
 O   |
/|   |
     |
     |     
=========
''',''' 
+---+
 |   |
 O   |
/    |
     |
     |     
=========
''',''' 
+---+
 |   |
 O   |
     |
     |
     |     
=========
''',''' 
+---+
 |   |
     |
     |
     |
     |     
=========
''']
name = input("What is your name? ")
print ("Hello, " + name, "Time to play hangman!")
lives=6
chosen_word=random.choice(words)

# print(chosen_word)
display=[]
for i in range(len(chosen_word)):
    display+='_'
print(display)
game_over=False
while not game_over:
    guessed_letter=input("Guess the letter ").lower()
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guessed_letter:
            display[position]=guessed_letter
    print(display)
    if guessed_letter not in chosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print("YOU LOSE!")
    if'_' not in display:
        game_over=True
        print("YOU WIN!")
    print(stages[lives])
