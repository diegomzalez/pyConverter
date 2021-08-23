from currency import CURRENCY_NAMES
"""
- [summary] The function displays a menu to user select a coin and enter its value.
"""
def menu () :
    i = True
    while i == True:
        currency_name = str(input("""
          
            ¿Qué moneda deseas convertir?
            -(VEF) to select VEF type: 'vef'.
            -(MXN) to select MXN type: 'mxn'.
            -(ARG) to select ARG type: 'arg'.
            -(COP) to select COP type: 'cop'.
            -(PNL) to select PNL type: 'pnl'.
            
             
             
            : """))
        if currency_name in CURRENCY_NAMES:
            while i == True:
                currency = float(input(f"¿Cuántos {currency_name} tienes?: "))
                if currency == float or int:
                    i = False
            i = False
    return currency_name, currency 
            
        