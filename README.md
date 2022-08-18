# Hangman

A game of hangman written in Python. 

Imported random package used initialisation of the class Hangman to select words randomly from a list. 

in check_letter, I chose to iterate through each letter of the answer, searching for the guessed letter while keeping count of index to account for cases in which one letter appears multiple times in a word.
This method doesnt stop when it reaches one instance of a correct letter, and iterates all the way through to the end of the word. 
Also keeping track of the index means that I could easily indicate which blank space "_" to fill in for word_guessed, because an index of the answer corrosponds to an index of word_guessed. 

The game could be customised by adding more words to word_list, but if you wanted to change the number of lives to anything more than 6 you'd have to add more graphics. 
But otherwise it would be easily customisable, and you could even lower the number of lives without having to change the graphics. 

