from app import *
import json

# load data from file in order to do test so fast
CurrenciesRate("data/eurofxref-hist-90d.xml")


def test_conversion():
    assert json.loads(Currency_Exchange({"amount": 1, "src_currency": "EUR", "dest_currency": "USD", "reference_date": "2020-04-15"}))["amount"] == 1.0903
    assert json.loads(Currency_Exchange({"amount": 1, "src_currency": "EUR", "dest_currency": "GBP", "reference_date": "2020-04-15"}))["amount"] == 0.87385
    assert json.loads(Currency_Exchange({"amount": 10, "src_currency": "GBP", "dest_currency": "EUR", "reference_date": "2020-04-15"}))["amount"] == 11.443611603822166
    assert json.loads(Currency_Exchange({"amount": 10, "src_currency": "EUR", "dest_currency": "USD", "reference_date": "2020-04-15"}))["amount"] == 10.903


def NullDateTest():
    assert json.loads(Currency_Exchange({"amount": 1, "src_currency": "EUR", "dest_currency": "USD", "reference_date": None}))["message"] == "Error date is not found!"


def InvalidDateTest():
    assert json.loads(Currency_Exchange({"amount": 1, "src_currency": "EUR", "dest_currency": "USD", "reference_date": "2030-01-01"}))["message"] == "Error date is not found!"


def InvalidCurrencyTest():
    assert  json.loads(Currency_Exchange({"amount": 1, "src_currency": None , "dest_currency": None, "reference_date": None}))["message"] == "Error Currency is not found!"
