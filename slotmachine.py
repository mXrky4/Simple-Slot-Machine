
import random

# Function Generates the row of the slot machine symbols
def spin_row():
    # A list of symbols roll of slot machine
    symbols = ['😁', '😎', '😆', '😏', '🤑']
    # For every symbols, pick a random 3 symbols
    return [random.choice(symbols) for _ in range(3)]

# Function: Prints the row that easy to read
def print_row(row):
    # Adding a string, which is a "|" in between the symbols output
    print("*************")
    print(" | ".join(row))
    print("*************")

# Function: Calculate the payout based on the row and bet
def get_payout(row, bet):
    #Creating a dictionary of row symbols and their value 
    payouts = {
        '😁':3, 
        '😎':4,
        '😆':5, 
        '😏':10, 
        '🤑':20
    }
    #If all row is equal or the same each other, get paid multiply by bets
    if row[0] == row[1] == row[2]:
        return bet * payouts.get(row[0], 0)
    return 0




# Main program
def main():
    balance= 100
    print("******************************************")
    print("Welcome to the Python Slots!")
    print("Symbols: 😁 - Smiley, 😎 - Cool, 😆 - Excited, 😏 - Smirk, 🤑 - Moneyface")
    print("******************************************")

    while balance > 0:
        print(f"Current balance: RM{balance}")

        bet =input("Make a bet amount (minimum RM5): ")

        if not bet.isdigit():
            print("Please enter a valid number.")
            continue #Reset the  main program

        bet = int(bet)

        if bet > balance:
            print("Insufficient fund")
            continue

        if bet <= 4:
            print("Bet must be higher than RM5")
            continue

        balance -= bet

        # Turning row into a list
        row = spin_row()
        print("Spinning......\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won RM{payout} ")
        else:
            print("Sorry you lost this round")

        balance += payout

if __name__ == '__main__':
    main()