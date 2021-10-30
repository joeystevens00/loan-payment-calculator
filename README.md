# Loan Payment Calculator

A CLI tool that calculates a loan's monthly payment, total interest payments, and total loan payments.

## Input fields
**amount**: Principal amount (e.g. 100000)

**interest**: Interest APR (e.g. 5.5%)

**downpayment**: Downpayment amount (e.g. 20000)

**term**: Term in years (e.g. 30)

## Output fields
**monthly_payment**: Amortized monthly loan payment

**total_interest**: Total interest paid over the lifetime of the loan

**total_payments**: Total payments over the lifetime of the loan

## Usage

Input should be in standard input formatted with the fields and values separated by a colon and each value separated by a new line. Outputs JSON

E.g.

```
$ echo "amount: 100000
interest: 5.5%
downpayment: 20000
term: 30 " | loan_payment_calculator
{'monthly_payment': 454.23, 'total_interest': 83523.23, 'total_payment': 163523.23}

```

## Installation
If poetry is already installed then just run `make` or `poetry install` otherwise install poetry with `make install_poetry` and load it into the env `source $HOME/.poetry/env`
