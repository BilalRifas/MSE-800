from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass
class Customer:
    customer_id: str
    first_name: str
    last_name: str
    email: str
    phone: str


@dataclass
class Currency:
    currency_code: str
    currency_name: str
    symbol: str


@dataclass
class ExchangeRate:
    base_currency: str
    quote_currency: str
    rate: Decimal
    effective_date: date


@dataclass
class Transaction:
    customer_id: str
    base_currency: str
    quote_currency: str
    amount_base: Decimal
    amount_quote: Decimal
    rate_used: Decimal
    transaction_date: date