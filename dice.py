#! /usr/bin/env python3
import numpy as np
from numpy.random import Generator, PCG64
from os import system

rnd = Generator(PCG64())

def main():
    print("Welcome to the CLI dice program! ('h' for help)")
    prev_command = ""
    while True:
        command = input("> ")
        if command == "":
            command = prev_command
        match command.lower():
            case "q":
                print("Thank you for using the CLI dice program!\n")
                break
            case "c":
                system("clear")
                continue
            case "h":
                print("""Help:
  XdY: Roll X dice with Y sides
       - X is optional and will default to 1, but Y is required
  c: clear the screen
  h: Show this help
  q: Quit\n""")
                continue
            case "":
                continue
            case _:
                if "d" not in command:
                    print("Error:\n  Unknown command.")
                    continue
                command_nums = command.split("d")
                try:
                    x = int(command_nums[0])
                except ValueError:
                    x = 1
                try:
                    y = int(command_nums[1])
                except ValueError:
                    print("Error:\n  The number of sides must be defined.\n")
                    continue
                try:
                    numbers = list(rnd.integers(1, high=y, size=x, dtype=np.uint64))
                except ValueError:
                    print("Error:\n  Invalid request.\n")
                    continue
                numbers_list = [str(i) for i in numbers]
                number_str = ", ".join(numbers_list)
                die_word = "dice"
                if x == 1:
                    die_word = "die"
                print(f"Rolling {x} {y} sided {die_word}:\n  {number_str} => {int(sum(numbers))}\n")
                prev_command = command


if __name__ == "__main__":
    main()
