from flask import Flask, request, render_template, redirect, session, flash

from forex_python.converter import RatesNotAvailableError
from forex_methods import curr_converter, convert_symbol, round_currency, cat_curr_symbol

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Sunniva046'

CURRENCY_LIST = []

def append_currency_list(converted_output):
    """appends exchange to list"""
    return CURRENCY_LIST.append(converted_output)

@app.route('/')
def forex_converter_home_page():
    """shows exchange form"""
    return render_template('index.html', final_list=CURRENCY_LIST)

@app.route('/check-currency-codes', methods=['POST'])
def check_currency_codes():
    """checks for the currency code and symbol and returns if found"""

    cvrt_from = request.form.get('convert-from').upper()
    cvrt_to = request.form.get('convert-to').upper()
    amnt = request.form.get('amount')

    try:
        CURRENCY_LIST.clear()
        converted_currency = curr_converter(cvrt_from, cvrt_to, amnt)
        rounded_currency = round_currency(converted_currency)
        converted_symbol = convert_symbol(cvrt_to)
        converted_output = cat_curr_symbol(converted_symbol, rounded_currency)
        append_currency_list(converted_output)
        flash("Exchanged!", 'success')
                
    except RatesNotAvailableError as exc:
        flash(f"{exc}", 'error')
    except ValueError as exc:
        str_exc = str(exc)
        exc_find = str_exc.find(':')
        exc_num = str_exc[exc_find::]
        flash(f"Please use a valid amount: {exc_num}!", 'error')

    return redirect('/')
