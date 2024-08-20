from app.roman_numerals import roman_to_decimal

for number in ('M', 'MD', 'MXCIII', 'MDCCXLVII', 'IV'):
    print(f'{number} -> {roman_to_decimal(number)}')