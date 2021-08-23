from currency import CURRENCY_VALUES
"""
- [summary] The function search the user coin selected and its value. 
"""
def selection(a, b):
    if a in CURRENCY_VALUES:
        dolar_value = CURRENCY_VALUES[a]
        currency = b
    return currency, dolar_value
    