from decimal import Decimal, InvalidOperation

import pandas as pd


def parse_money(value, field_name="Amount"):
    """Read finite money with at most two decimal places; never round input silently."""
    try:
        amount = Decimal(str(value).strip())
        if not amount.is_finite():
            raise ValueError(f"{field_name} must be a finite number.")
        cents = amount.quantize(Decimal("0.01"))
        if amount != cents:
            raise ValueError(f"{field_name} must have at most two decimal places.")
        return cents
    except (InvalidOperation, TypeError) as error:
        raise ValueError(f"{field_name} must be a valid monetary amount.") from error


class Finance:
    """Calculates payments and records income from completed sales."""

    COLUMNS = ["sale_id", "amount", "date"]

    def __init__(self, income_df=None):
        self.income_df = income_df if income_df is not None else pd.DataFrame(columns=self.COLUMNS)
        self.amount_received = Decimal("0")
        self.change = Decimal("0")

    def process_payment(self, total, amount_received):
        total = parse_money(total, "Total")
        amount_received = parse_money(amount_received, "Amount received")
        if total <= 0:
            raise ValueError("Total must be greater than zero.")
        if amount_received < total:
            raise ValueError(f"Insufficient payment. {total - amount_received:.2f} more is needed.")

        self.amount_received = amount_received
        self.change = amount_received - total
        return self.change

    def record_income(self, sale_summary):
        row = {
            "sale_id": sale_summary["sale_id"],
            "amount": str(sale_summary["total"]),
            "date": sale_summary["sale_date"],
        }
        self.income_df = pd.concat([self.income_df, pd.DataFrame([row])], ignore_index=True)
