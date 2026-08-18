#DAY 7
import random
import words
def lose_image(chance_till_game_lost):
   if chances_till_game_lost==1:
      print('''
  +---+
  |   |
  O   |
      |
      |
      |
=========''')
   elif chances_till_game_lost==2:
      print('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''')
   elif chances_till_game_lost==3:
      print('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''')
   elif chances_till_game_lost==4:
      print('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''')
   elif chances_till_game_lost==5:
      print('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''')
   elif chances_till_game_lost==6:
      print('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''')
print(''' ____   ____       _____  _____   ______         _____         ______  _______         _____  _____   ______   
|    | |    |  ___|\    \|\    \ |\     \    ___|\    \       |      \/       \    ___|\    \|\    \ |\     \  
|    | |    | /    /\    \\\    \| \     \  /    /\    \     /          /\     \  /    /\    \\\    \| \     \ 
|    |_|    ||    |  |    |\|    \  \     ||    |  |____|   /     /\   / /\     ||    |  |    |\|    \  \     |
|    .-.    ||    |__|    | |     \  |    ||    |    ____  /     /\ \_/ / /    /||    |__|    | |     \  |    |
|    | |    ||    .--.    | |      \ |    ||    |   |    ||     |  \|_|/ /    / ||    .--.    | |      \ |    |
|    | |    ||    |  |    | |    |\ \|    ||    |   |_,  ||     |       |    |  ||    |  |    | |    |\ \|    |
|____| |____||____|  |____| |____||\_____/||\ ___\___/  /||\____\       |____|  /|____|  |____| |____||\_____/|
|    | |    ||    |  |    | |    |/ \|   ||| |   /____ / || |    |      |    | / |    |  |    | |    |/ \|   ||
|____| |____||____|  |____| |____|   |___|/ \|___|    | /  \|____|      |____|/  |____|  |____| |____|   |___|/
  \(     )/    \(      )/     \(       )/     \( |____|/      \(          )/       \(      )/     \(       )/  
   '     '      '      '       '       '       '   )/          '          '         '      '       '       '   
                                    '                                                           ''')
#umported from words.py
target_word=random.choice(words.words)
chances_till_game_lost=0
x=len(target_word)
guessed=[0 for i in range(x)] #create an list full of zeroes as per number of letters in target_word -->0 is replaced by correctly guessed letter
game_over=False
#game_over set to false for while loop
letters=[i for i in target_word]
while(not game_over): 
    guess_letter=input("guess an letter:")
    if guess_letter in letters:
        n=letters.index(guess_letter)
        guessed[n]=guess_letter
        for i in guessed:
           if i==0: 
            print("_",end=" ")  #to simulate _ _ _ _ _ a _ for example
           else:
            print(i,end=" ")
        if 0 not in guessed:
           game_over=True
        if not game_over:  #to skip rest of current iteration of the while loop use continue keyword
          continue
    else:
       chances_till_game_lost+=1 #total 6 chances in an hangman game
       lose_image(chances_till_game_lost)
       if chances_till_game_lost==6:
          print("GAME OVER")
          break
       continue