from typing import Union

from pydantic import BaseModel


class LoanPaymentCalculation(BaseModel):
    monthly_payment: float
    total_interest: float
    total_payment: float


class LoanPaymentQuery(BaseModel):
    amount: int
    interest: Union[str, float]
    downpayment: int
    term: int

    @classmethod
    def from_dirty_input(cls, **attrs):
        attrs = {k.lower().strip(): v.strip() for k, v in attrs.items()}
        return cls(**attrs)

    def interest_decimal(self):
        if isinstance(self.interest, str) and '%' in self.interest:
            return float(self.interest.split('%')[0])/100
        self.interest = float(self.interest)
        if self.interest > 1:
            return self.interest / 100
        return self.interest

    @classmethod
    def amortized_loan_payment(cls, principal, annual_rate, loan_years):
        a = principal
        r = annual_rate/12
        n = loan_years*12
        return a/((((1+r) ** n)-1)/(r*(1+r)**n))

    @property
    def monthly_payment(self):
        return self.amortized_loan_payment(
            self.amount-self.downpayment,
            self.interest_decimal(),
            self.term
        )

    def calculate(self) -> LoanPaymentCalculation:
        monthly_payment = self.monthly_payment
        total_payment = monthly_payment * self.term * 12
        total_interest = total_payment - self.amount + self.downpayment
        return LoanPaymentCalculation(
            monthly_payment=round(monthly_payment, 2),
            total_interest=round(total_interest, 2),
            total_payment=round(total_payment, 2),
        )
