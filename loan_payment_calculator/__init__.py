import sys

from .calculate import LoanPaymentQuery

def cli():
    input = sys.stdin.read()
    parsed_input = {}
    for line in input.split("\n"):
        if ':' in line:
            field, value = line.split(':')
            parsed_input[field] = value
    calculated_loan_payment = LoanPaymentQuery.from_dirty_input(**parsed_input).calculate()
    print(dict(calculated_loan_payment))
