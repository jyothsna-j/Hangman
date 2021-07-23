import random
moviesList = ["Avengers-Endgame", "Black Widow", "Terminator", "Conjuring", "Evil Dead", "Shutter Island", "Inception", "Interstellar"]
x = random.randint(0, len(moviesList)-1)
movie = moviesList[x]
copy, c = list(movie), movie.lower()
for i in range(len(copy)):
    if copy[i] not in "AEIOUaeiou -":
        copy[i]="-"
guess = 10
print("WELCOME TO HANGMAN")
while True:
    flag = True
    print("\n","".join(copy))
    print("You have",guess,"guesses.")
    tryy = input("Enter your guess: ")
    while tryy in c:
        flag = False
        p = c.find(tryy)
        copy[p]=tryy
        c = c.replace(tryy, '#', 1)
    if flag == True:
        guess = guess - 1
        print("\nwrong guess :(")
    if guess == 0:
        print("\n\nOops! YOU LOSE \nBetter luck next time!\nThe movie is", movie)
        break
    if "".join(copy).lower() == movie.lower():
        print("\n\nCONGRATS! YOU WON\nThe movie is",movie,"\nYou get a slice of cheese :p")
        break
