import random         #for random numbers 
import hangman_stages
word_list=['apple','mango','potato','pineapple','beautiful']
lives=6
chosen_word=random.choice(word_list)
print(chosen_word)
display=[]
for i in range(len(chosen_word)):         #0,1,2,3,4,5
    display += '-'              #because for every word it will provide a dash to choose which alphabet we have to gusse
print(display)   
game_over=False
while not game_over:
    guessed_letter=input("guess a letter:") 
    for position in range (len(chosen_word)):
        letter=chosen_word[position]
        if letter==guessed_letter:
            display[position]=guessed_letter
    print(display)
    if guessed_letter not in chosen_word:
        lives -=1 
        if lives==0:
            game_over=True
            print("tou lose!!")
    if "-" not in display:
        game_over=True
        print("you won")       
            
    print(hangman_stages.stages[lives]) 
       
            
            
            
            







     