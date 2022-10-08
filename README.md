
# LCR Simulator

LCR is a dice game, one of pure chance. Therefore, we can write a simulator to avoid wasting the time playing it ourselves.

> Each player receives at least 3 chips. Players take turns to roll three six-sided die, each of which is marked with an "L", "C", and "R" on one side, and a single dot on the three remaining sides. For each "L" or "R" thrown, the player must pass one chip to the player to their left or right, respectively. A "C" indicates a chip to the center (pot). A dot has no effect.
____________________________________________________________________________________
>If a player has fewer than three chips left, they are is still in the game but their number of chips is the number of dice they can roll on their turn, rather than rolling all three. When a player has zero chips, they pass the die on their turn, but may receive chips from others and take their next turn accordingly. The winner is the last player with chips left. They do not roll the dice, and win the center pot. If they choose to play another round, they do not roll 3, they keep their pot and play with that.

When the program starts, it should ask for the names of the players, until the user enters 'done'. Then it should run the simulation, tell the user who won, and ask the player whether they'd like to play again.
