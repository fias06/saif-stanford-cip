import random as ran

movies = ["avatar", "avengers", "pathaan", "gladiator", "spiderman", "thor", "godfather", "troy"]


print("WELCOME TO THE HANGMAN MOVIE QUIZ\nYou have 5 lives\n")

rand_mov = ran.choice(movies)


lives = 5
turns = 0

def photos():
    if lives == 5:
        print("""\n
  ____
  |   |
      |
      |
      |
      |
 ------
        \n\n""")
    elif lives == 4:
        print("""\n
  ____
  |   |
  0   |
      |
      |
      |
 ------ \n\n""")
    elif lives == 3:
        print("""\n
  ____
  |   |
  0   |
  |   |
      |
      |
 ------\n\n""")
    elif lives ==2:
        print("""\n
  ____
  |   |
  0   |
 /|\  |
      |
      |
 ------ \n\n""")
    elif lives == 1:
        print("""\n
  ____
  |   |
  0   |
 /|\  |
 /   |
      |
 ------\n\n""")
    elif lives == 0:
        print("""\n
  ____
  |   |
  0   |
 /|\  |
 / \  |
      |
 ------\n\n""")





photos()
for i in rand_mov:
    if i.isalpha():
        print(" _ ", end=" ")

guess = []

while lives>0:
    ans = input("\n\nEnter a letter or a word: ")
    if ans.lower() == rand_mov:
        print(rand_mov)
        print("\n\nCONGRATS, you won the game")
        turns += 1
        print("Number of turns: ", turns)
        print("Number of lives left: ", lives)
        break

    elif ans.lower() in rand_mov:
        print("You guessed it right!")
        turns += 1
        
        guess.append(ans.lower())

        opt = []
        for a in rand_mov:
            if a in guess:
                opt.append(a)
            else:
                opt.append(" _ ")
        opt2 = " ".join(opt)
        opt3 = "".join(opt)
        
        if opt3 == rand_mov:
            print("\nYou won the game")
            print("The movie was ", rand_mov)
            print("Number of turns: ", turns)
            print("Number of lives left: ", lives)
            break
        print(opt2)
        print("\n\nNumber of lives left: ", lives)
        print("Number of turns taken: ", turns)
        
        photos()
                
        

    elif ans not in rand_mov:
        guess.append(ans)
        print("\n\nSorry, you did not guess it right!")
        turns += 1
        lives -=1
        opt = []
        for a in rand_mov:
            if a in guess:
                opt.append(a)
            else:
                opt.append(" _ ")
        opt2 = " ".join(opt)
        print(opt2)
        print("\nNumber of lives left: ", lives)
        print("Number of turns taken: ", turns)
        photos()
else:
    print("\n\nYou lost!! Better luck next time")
    print("The movie was ", rand_mov)
        
        

    

