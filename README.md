HANGMAN

This is a recreation of the popular guessing game, Hangman, using Python.

The computer selects one random word from a list, and you need to try to guess it!

The game is played via Terminal currently. The user will need to input either one letter (case insensitive), or an '*' (explained below). 

The game starts off with 6 tries (guesses), and 3 warnings. The warnings will appear if the user puts in invalid input, such as strings of texts longer than 1 character, or any other invalid characters (numbers, symbols). The only exception is when the user inserts '*', which symbolizes the 'Hint' button.

If the letter selected is not part of the word, and depending on the type (consonant or vowel), the user will be penalized with 1 or 2 guesses respectively.
I.E. I guess the letter 'e', and the word is 'ultra', I would be left with 4 guesses instead

The hint button ('*') will return a list of all available words that would match the length and letter structure that is currently present.

If the user loses, they will be prompted with a message saying the game is over.

If the user wins, they will be congratulated, and receive the final score (calculated based on the number of tries needed and the overall complexity of the word).

***********
This project may be expanded upon, adding a GUI would be the first idea.