#!/usr/bin/env python
from decimal import Decimal

def plus(a, b): 
	return a + b

def minus(a, b): 
	return a - b

def multiplied(a, b): 
	return a * b

def divide(a, b):
	return a / b

calc = {
	'+': plus,
	'-': minus,
	'*': multiplied,
	'/': divide
	}

operators = tuple(calc.keys())


def main():
	print('Calculator. ver 1.0'.center(50, '='))
	while True:
		expr = raw_input('Enter a expression (q for exit): ')
		if (expr.lower()) == 'q':
			break
		try:
			#finding sign
			sign = ''
			for c in expr:
				if c in operators:
					sign = c
			temp = expr.partition(sign)

			result = calc[sign](Decimal(temp[0].strip()),
				Decimal(temp[-1].strip()))

			print('Answer: {0}'.format(result))
		except ZeroDivisionError:
			print('Error: division by zero')
		except Exception:
			pass

if __name__ == '__main__':
	main()