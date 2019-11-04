"""Write a function called 'add_interest()' which calculates the balance of a
savings account given an initial balance and an annual interest rate (in
percent). Use that function to calculate the total savings in function
'savings()' after N years, again given an initial deposit and a fixed annual
interest rate.
"""


def savings(years, initial_deposit, annual_interest_rate):
    return (
        initial_deposit * ((annual_interest_rate + 100) / 100) ** years
    )


def add_interest(initial_balance, annual_interest_rate):
    return savings(1, initial_balance, annual_interest_rate)
