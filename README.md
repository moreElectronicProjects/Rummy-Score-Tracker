# Rummy Score Track

This is a simple program which keeps track of a game of 500 Rummy. It keeps track of who is dealing the deck, each player's score per round, and the total player score. When a player has the highest score, over 500, and is not tied with anyone else, the program displays the winner and exits.

# Running the Program

This program is designed to be ran using Python 3. No additionally dependencies are required.

Note: running this program on Windows will cause an error when the program attempts to clear the screen. To fix this error, change the command on line 5,

from

```
clear_screen_command = "clear"
```

to

```
clear_screen_command = "cls"
```

# How to Change a Score of a Player

If a player's score has been entered incorrectly, typing the word "change" will allow a score to be changed.
