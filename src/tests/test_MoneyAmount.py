import pytest

from src.Currency import Euro
from src.MoneyAmount import MoneyAmount
from src.tests.CurrencyStub import EuroStub, DollarStub

USD = DollarStub()

def test_test_amount_cannot_be_negative():
    with pytest.raises(ValueError):
        MoneyAmount(-1, USD)

def test_has_nice_string_representation():
    assert str(MoneyAmount(100, USD)) == "100 USD"

def test_should_add_amounts_of_same_currency():
    assert (MoneyAmount(100, USD) + MoneyAmount(50, USD)
            ==
            MoneyAmount(150, USD))

def test_bigger_amount_is_greater_than_smaller_amount():
    assert MoneyAmount(100, USD) > MoneyAmount(50, USD)

def test_bigger_amount_is_greater_than_smaller_amount_for_different_currencies():
    assert MoneyAmount(100, USD) > MoneyAmount(10, Euro())

def test_conversion():
    assert MoneyAmount(100, EuroStub()).convert_to(USD) == MoneyAmount(110, USD)
