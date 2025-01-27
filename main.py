from constants import STATE_TAXES

def get_income():
    while True:
        income = input('Annual Income: ')
        try:
            income = int(income)
        except ValueError:
            print('Input must be an integer and greater than 0')
            continue
        if 0 < income:
            return income
        else:
            print('Input must be an integer and greater than 0')

def get_state():
    while True:
        state = input('State: ')
        try:
            STATE_TAXES[input.upper()]
        except ValueError:
            print("")

def main():
    income = get_income()
    print(f"Your income is: {income}")

if __name__ == "__main__":
    main()