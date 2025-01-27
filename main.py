from constants import STATE_TAXES, FEDERAL_TAX_BRACKETS

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

def get_offer():
    while True:
        offer = input('Offered Salary: ')
        try:
            offer = int(offer)
        except ValueError:
            print('Input must be an integer and greater than 0')
            continue
        if 0 < offer:
            return offer
        else:
            print('Input must be an integer and greater than 0')

def get_state():
    while True:
        state = input("Enter the two-letter state abbreviation (e.g., 'UT', 'AZ', 'NV'): ").strip().lower()
        if state in STATE_TAXES:
            return state
        else:
            print("Invalid input. Please enter a valid two-letter state abbreviation.")

def find_tax_rate(value):
    for bracket in FEDERAL_TAX_BRACKETS:
        if bracket in FEDERAL_TAX_BRACKETS:
            if bracket ['min'] <= value <= bracket['max']:
                return bracket['rate']
    return None

def perform_calculation():
    income = get_income()
    offer = get_offer()

    income_rate = find_tax_rate(income)
    offer_rate = find_tax_rate(offer)

    current_take_home = income - (income * income_rate)
    projected_take_home = offer - (offer * offer_rate)

    print(f"Your current take home pay is ${current_take_home:,.2f}")
    print(f"Your projected take home pay is ${projected_take_home:,.2f}")
    
    min_offer = current_take_home / (1 - offer_rate)

    print(f"Advise: An offer of {min_offer:,.2f} or higher is best")

def main():
    perform_calculation()

if __name__ == "__main__":
    main()