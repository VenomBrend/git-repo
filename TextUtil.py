#!usr/bin/env/ python3
#Copyright (c) 2008

#"""
#>>>> is_balanced("(Python (is (not (lisp))))")
#True
#>>>> shorten("The Crossing", 10)
#"The Cro..."
#"""
#>>>>simplify(" some text with spurious whitespaces  ")
#"some text with spurious white spaces"
#"""

import string

def shorten(text, length=25, indicator='...'):
	if len(text) > length:
		return text[:length - len(indicator)] + indicator
	else:
		return text


def simplify(text, whitespace=string.whitespace, delete=""):
	r""" Return the text there are all spaces were deleted

	whitespace - строка символів, кожний елемент якої вважається
	символом пробела.  Якщо delete не порожній, кожний символ цієї строки
	буде видалений із вихідної text
	>>>> simplify(" this and \n that \n too")
	'this and that too'
	>>>> simplify(" Washington D.C. \n")
	'Washington D.C.'
	>>>> simplify(" Washington D.C. \n", delete=",;.:")
	'Washington DC'
	>>>> simplify("  abcdrf  ssd  ", delete="abcd")
	'rf ss'

	"""
	result = []
	word = ''
	for char in text:
		if char in delete:
			continue
		elif char in whitespace:
			if word:
				word += char
				result.append(word)
				word = ""
		else:
			word += char
	if word:
		result.append(word)
	if result[-1][-1] in whitespace:
		result[-1] = result[-1].strip(whitespace)
	return "".join(result)


def is_balanced(text, brackets="()[]{}<>"):
	counts = {}
	left_for_right = {}
	for left, right in zip(brackets[::2], brackets[1::2]):
		assert left != right, "the bracket charaster must differ"
		counts[left] = 0
		left_for_right[right] = left
	for c in text:
		if c in counts:
			counts[c] += 1
		elif c in left_for_right:
			left = left_for_right[c]
			if counts[left] == 0:
				return False
			counts[left] = -1
	return not any(counts.values())



if __name__ == "__main__":
	import doctest
	doctest.testmod()
