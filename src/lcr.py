"""
Author: Hunter, Christerpher
Date: 2022 OCT 08
Description: This program will simulate the dice game of LCR.
"""

import random


def user_inquiry() -> list[str]:
    """Ask for the names of the players until 'done' is entered."""

    # Initialize list of players
    players = []

    # Ask for players until 'done' is entered
    while True:
        player = input("Enter player name (or 'done'): ")
        if player == 'done':
            break
        players.append(player)

    return players


# play again?
def play_again() -> bool | None:
    """Ask the user if they want to play again."""

    answer = input("Do you want to play again? (y/n): ")
    if answer in ['y', 'n']:
        return answer == 'y'
    elif not isinstance(answer, str):
        raise ValueError("Please enter 'y' or 'n'.")
    else:
        raise ValueError("Please enter 'y' or 'n'.")


def roll_sixed_sided_die() -> int:
    """Roll a six sided die and return the result."""

    dice_roll_algo: int = random.randint(1, 6)

    return dice_roll_algo


def l_c_r(rolled_die: int) -> bool:
    """Return True if the die roll is an L, C, or R."""

    l_c_r_sides_already_acounted_for: list[int] = [
        1,
        2,
        3,
        4,
        5,
        6
    ]

    side_r: dict[str, int] = {
        'R': random.choice(l_c_r_sides_already_acounted_for),
    }

    l_c_r_sides_already_acounted_for.remove(side_r['R'])

    side_l: dict[str, int] = {
        'L': random.choice(l_c_r_sides_already_acounted_for),
    }

    l_c_r_sides_already_acounted_for.remove(side_l['L'])

    side_c: dict[str, int] = {
        'C': random.choice(l_c_r_sides_already_acounted_for),
    }

    match = {
        'R': rolled_die == side_r['R'],
        'L': rolled_die == side_l['L'],
        'C': rolled_die == side_c['C']
    }

    return match['R'] or match['L'] or match['C']


def main() -> None:

    # how long does it take to run the program?
    import time
    start_time = time.time()

    # Calculate the percentage of wins for each roll
    win_count: int = int()
    for _ in range(1_000):
        if l_c_r(roll_sixed_sided_die()):
            win_count += 1
    print(f"Win percentage: {(win_count / 1000) * 100}%")

    # how long does it take to run the program?
    print(f"--- {time.time() - start_time:.5f} seconds ---")


if __name__ == '__main__':
    main()
