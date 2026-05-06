"""
Unstructured unit tests without a unit test framework
Rather than asserting, the user must check out the results manually
"""

from app.roman_numerals import roman_to_decimal

for number in ('M', 'MD', 'MXCIII', 'MDCCXLVII', 'IV'):
    print(f'{number} -> {roman_to_decimal(number)}')