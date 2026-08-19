#DAY 7
import random
import words
clue=words.clues
def lose_image(chances_till_game_lost):
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
                                                      #imported from words.py on the project directory
target_word=random.choice(words.words)
word_index_position=words.words.index(target_word)    #to get the index position where the word is in the words list from words.py so we can get the corresponding clue for this word
clue=words.clues[word_index_position]                 #to save the clue of corresponding word on this variable to print it later down the line
chances_till_game_lost=0                              #total 6 chances
length_of_the_target_word=len(target_word)            
guessed=["_" for i in range(length_of_the_target_word)]#create an list full of _ as per number of letters in target_word -->0 is replaced by correctly guessed letter
game_over=False                                        #game_over set to false for while loop
letters=[i for i in target_word]                       #list comprenhension list of letters of target_word
print("the clue for the given word is :",clue)
while(not game_over): 
    guess_letter=input("guess an letter:").lower()   #so no matter what user gives caps letter or small , the input is taken as small letter because thats how it is on the words list on words.py
    if guess_letter in letters:                      #.count() method returns the count of certain value on an iterable
        for i in range(letters.count(guess_letter)): #if apple , user guessed p , by rules of hangman its , _ p p _ _, all the slots of that letter must be filled thats why im implementing this logic
          n=letters.index(guess_letter)              # .index() method returns index position of first occurance of the guess_letter on the list letters
          guessed[n]=guess_letter                    #fixing this with my own implementation avaoiding chatGPT blindily
          letters[n]=-1                                 #because letters in the letters list can be repeated , to account to repeaticility
        for i in guessed:
           print(i,end=" ")
        if "_" not in guessed:                        #condition to check if all the blanks are filled(Winning criteria)
           print("\n\nGAME OVER YOU WON")             #\n is the newline charecter
           game_over=True                             #loop stop condition
    else:
       chances_till_game_lost+=1                      #total 6 chances in an hangman game
       lose_image(chances_till_game_lost)
       if chances_till_game_lost==6:
          print("GAME OVER YOU LOST")
          print("\n\nTHE WORD WAS",target_word)
          game_over=True                              #loop stop condition
      

