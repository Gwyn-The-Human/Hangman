



list_letters = ["A","B"]


class Hongman:


    def __init__(self, word_list, num_lives=5):
        print ("init")
        

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




