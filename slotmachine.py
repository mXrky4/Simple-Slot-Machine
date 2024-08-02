# Function Generates the row of the slot machine symbols
def spin_row():
    #A list of symbols roll of slot machine
    symbols = ['😁', '😎', '😆', '😏', '🤑']
    return [random.choice(symbols), for_ in range(3)]

# Function: Prints the row that easy to read
def print_row():
    pass

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




# Game start
def main():
    balance= 100
    print("******************************************")
    print("Welcome to the Python Slots!")
    print("Symbols: 😁 - Smiley, 😎 - Cool, 😆 - Excited, 😏 - Smirk, 🤑 - Moneyface")
    print("******************************************")

    while balance > 0:
        print(f"Current balance: RM{balance}")

        bet =input("Make a bet (minimum RM5): ")

        if not bet.isdigit():
            print("Please enter a valid number.")
            continue


main()