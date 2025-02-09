import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count ={
	"A" : 2,
	"B" : 4,
	"C" : 6,
	"D" : 8	
}

symbol_value = {
	"A" : 5,
	"B" : 4,
	"C" : 3,
	"D" : 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbols] * bet
            winning_lines.append(line + 1)
                
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
           
    
        columns.append(column)
        
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end="|")
            else:
                print(column[row], end="")
            
        print()


def deposit():
    while True:
        amount = input("Enter amount to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else: 
                 print("amount must be more than $0")
        else:
            print("Enter a digit")
    return amount


     
def get_number_of_lines():
    while True:
        lines = input("Enter number of lines to bet on, (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a number")
        else:
            print("Enter a digit")
    return lines
    
    


def get_bet():
    while True:
        amount = input("Enter amount you'd like to to bet on each line: $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                	break
            else: 
                print(f"Amoung must be between ${MIN_BET} and ${MAX_BET}")
        else:
            print("Enter a digit")
    return amount




def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total = bet * lines
        if total > balance:
            print("Sorry, you do not have enough balance")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total}")





    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)        
    return winnings - total     



def main():
    balance = deposit()
    while True:
        print(f"current balance is ${balance}")
        prompt = input("Press Enter to play and 'q' to quit")
        if prompt == "q":
            break
        balance += spin(balance)

    print(f"You are left with ${balance}")
    

main()
