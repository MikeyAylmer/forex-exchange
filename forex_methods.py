from forex_python.converter import CurrencyRates, CurrencyCodes
from forex_python.converter import RatesNotAvailableError

c_convert = CurrencyRates()
c_codes = CurrencyCodes()

def curr_converter(con_from, con_to, amount):
    """converts currency"""
    if not c_codes.get_symbol(con_from):
        raise RatesNotAvailableError(f"{con_from} is not a valid curren$y!")
    if not c_codes.get_symbol(con_to):
        raise RatesNotAvailableError(f"{con_to} not a valid curren$y!")
    if int(amount):
        return c_convert.convert(con_from, con_to, int(amount))
    if float(amount):
        return c_convert.convert(con_from, con_to, float(amount))
    else:
        raise ValueError
    
def round_currency(con_curr):
    """rounds coverted currency"""
    res = int(con_curr)
    return round(con_curr, 2)

def convert_symbol(con_to):
    """changes code to symbol"""
    return c_codes.get_symbol(con_to)


def cat_curr_symbol(con_symbol, rounded_curr):
    """concatenate symbol with currency"""
    return f"{con_symbol}{rounded_curr}"