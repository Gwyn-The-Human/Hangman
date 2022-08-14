
from re import X


list_letters = ["A","B"]


class Hongman:

    def check_letter ():
        print ("Guess a new letter!")
        letter = input ().upper() #will the guess be case sensitive? keep .upper in mind!! 
        if len(letter) != 1:
            print ("Please, enter just one character.")
            return Hongman.check_letter()
        if letter in list_letters:
            print (f"{letter} has already been tried.")
            return Hongman.check_letter()
        return letter

x = Hongman.check_letter()

print (x + " is my guess!")