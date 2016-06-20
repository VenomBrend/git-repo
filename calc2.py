#!/usr/bin/env python
from __future__ import print_function
from decimal import Decimal, DivisionByZero
import cgi
import cgitb
cgitb.enable()


def plus(a, b): 
	return a + b

def minus(a, b): 
	return a - b

def multiplied(a, b): 
	return a * b

def divide(a, b):
	if b == 0: raise DivisionByZero
	return a / b

calc = {
	'+': plus,
	'-': minus,
	'*': multiplied,
	'/': divide
	}

form = cgi.FieldStorage()
firstNum = form['text1'].value
sign = form['sign'].value
secondNum = form['text2'].value

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Result</title>
        </head>
        <body>""")
try:
	result = calc[sign](Decimal(firstNum), Decimal(secondNum))
	print("<h1>{0} {1} {2} = {3}</h1>".
		format(firstNum, sign, secondNum, result))
except DivisionByZero:
	print("<h1>Error: division by zero</h1>")
print("""</body>
        </html>""")