"""
- [summary] The function convert user currency to dollars.
"""
def converter (b, c) :
    dollars = round(b / c, 2)
    print(f"Tienes: {dollars} USD!")
    