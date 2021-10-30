from loan_payment_calculator.calculate import LoanPaymentQuery

import pydantic
import pytest

test_queries = [
    LoanPaymentQuery(amount=100_000, interest="5.5%", downpayment=20_000, term=30),
    LoanPaymentQuery(amount=350_000, interest="3.5%", downpayment=70_000, term=20),
    LoanPaymentQuery(amount=500_000, interest="3.7%", downpayment=125_000, term=30)
]


@pytest.mark.parametrize(
    "input,expected_interest_decimal",
    [
        ("5.5%", 0.055),
        (0.05, 0.05),
        (5.5, 0.055),
    ],
)
def test_interest_decimal(input, expected_interest_decimal):
    assert LoanPaymentQuery(amount=100_000, interest=input, downpayment=15_000, term=10).interest_decimal() == expected_interest_decimal


@pytest.mark.parametrize(
    "input,expected_calculation",
    list(zip(test_queries, [
        {'monthly_payment': 454.23, 'total_interest': 83523.23, 'total_payment': 163523.23},
        {'monthly_payment': 1623.89, 'total_interest': 109732.93, 'total_payment': 389732.93},
        {'monthly_payment': 1726.06, 'total_interest': 246382.03, 'total_payment': 621382.03},
    ]))
)
def test_calculate(input, expected_calculation):
    print(input, dict(input.calculate()), expected_calculation)
    assert dict(input.calculate()) == expected_calculation


@pytest.mark.parametrize(
    "input,expected",
    [
        (dict(), pytest.raises(pydantic.error_wrappers.ValidationError)),
        (dict(amount="a", interest="5.5%", downpayment=20_000, term=30), pytest.raises(pydantic.error_wrappers.ValidationError)),
        (dict(amount=100_000, interest="5.5%", downpayment="a", term=30), pytest.raises(pydantic.error_wrappers.ValidationError))
    ]
)
def test_calculate_invalid(input, expected):
    with expected:
        LoanPaymentQuery(**input)
