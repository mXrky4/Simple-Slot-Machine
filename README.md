# Python Slots Game

Welcome to the Python Slots Game! This is a simple slot machine game implemented in Python that you can run directly from your terminal. Spin the reels, place your bets, and see if you can win big!

## Features

- Five unique symbols: 😁 (Smiley), 😎 (Cool), 😆 (Excited), 😏 (Smirk), 🤑 (Moneyface)
- Simple betting system with payouts based on the symbols
- Keeps track of your balance and allows multiple rounds of play
- User-friendly interface with clear instructions

## How to Run

1. **Install Python**: Make sure Python 3.12 is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Download the Script**: Clone this repository or download the script file `slotmachine.py` from the repository.

   ```bash
   git clone https://github.com/maljunkul/Simple-Slot-Machine.git
   cd Simple-Slot-Machine
    ```

3. **Run the Script**: Open your terminal or command prompt, navigate to the directory containing slots_game.py, and execute the script:
    ```bash
    python slotmachine.py
    ```

## Gameplay Instructions
**Start the Game**: Upon starting, the game will display a welcome message and show the available symbols with their descriptions.

**Place Your Bet**: Enter the amount you wish to bet. Note that the minimum bet is RM5.

**Spin the Reels**: The slot machine will spin the reels and display the result after a brief pause.

**Check Your Winnings**: If all three symbols in a row match, you win a payout based on the symbol and your bet amount. The payout values are:

**😁 (Smiley)** - 3x your bet <br/>
**😎 (Cool)** - 4x your bet <br/>
**😆 (Excited)** - 5x your bet <br/>
**😏 (Smirk)** - 10x your bet <br/>
**🤑 (Moneyface)** - 20x your bet <br/>

**Play Again**: After each spin, you can choose to play another round or exit the game. Your balance will be updated based on your winnings or losses.

**End the Game**: The game ends when you choose not to play again or when your balance reaches zero. Your final balance will be displayed.