import random
MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1
ROWS = 3
COLS = 3
symbol_count = {
    "Aj": 2,
    "Dr": 4,
    "Av": 6,
    "Js": 8
}
symbol_value = {
    "Aj": 5,
    "Dr": 4,
    "Av": 3,
    "Js": 2
}
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            if column[line] != symbol:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols += [symbol] * count
    columns = []
    for _ in range(cols):
        current_symbols = all_symbols[:]
        column = []
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()
def deposit():
    while True:
        amount = input("How much do you want to deposit?\n: $")
        if amount.isdigit():
            amount = int(amount)
            if 0 <= amount <= 1000:
                break
            else:
                print("Amount must be greater than 0 and upto 1000!")
        else:
            print("Please enter a valid number!")
    return amount
def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines you want to bet on (1 - {MAX_LINES})\n: ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines!")
        else:
            print("Please enter a number!")
    return lines
def get_bet():
    while True:
        amount = input("How much do you want to bet on the lines?\n: $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Bet must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a valid number!")
    return amount
def game(balance):
    no_of_lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * no_of_lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {no_of_lines} lines. Total bet is: ${total_bet}")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, win_lines = check_winnings(slots, no_of_lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    if win_lines:
        print("You won on lines:", *win_lines)
    else:
        print("No winning lines this time.")
    return winnings - total_bet
def main():
    balance = deposit()
    while True:
        print(f"\nCurrent balance is ${balance}")
        spin = input("Press enter to play (q to quit): ")
        if spin.lower() == 'q':
            break
        balance += game(balance)
    print(f"\nYou left with ${balance}")
main()
