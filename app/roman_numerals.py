"""
Conversion from Roman numeral to decimal

v1.0.0 August 2024
v1.1.0 September 2024. Specification checks added
"""
__author__ = "Arturo Mora-Rioja"
__version__ = "1.1.0"

def roman_to_decimal(number: str) -> int:
    error_message = 'Badly formed Roman numeral'

    # Invalid symbols are removed from the string
    clean_number = []
    for letter in number:
        if letter in ['M', 'D', 'C', 'L', 'X', 'V', 'I']:
            clean_number.append(letter)
    number = ''.join(clean_number)

    # V, L and D can never be repeated
    if number.count('V') > 1 or number.count('L') > 1 or number.count('D') > 1:
        raise Exception(error_message)

    # No digit can be repeated more than 3 times in a row
    if 'MMMM' in number or 'CCCC' in number or 'XXXX' in number or 'IIII' in number:
        raise Exception(error_message)

    # D cannot precede M
    if 'DM' in number:
        raise Exception(error_message)

    # L cannot precede M, D or C
    if 'LM' in number or 'LD' in number or 'LC' in number:
        raise Exception(error_message)

    # V cannot precede M, D, C, L or X
    if 'VM' in number or 'VD' in number or \
       'VC' in number or 'VL' in number or 'VX' in number:
        raise Exception(error_message)

    # X cannot precede D
    if 'XD' in number:
        raise Exception(error_message)

    # I cannot precede M, D, C or L
    if 'IM' in number or 'ID' in number or \
       'IC' in number or 'IL' in number:
        raise Exception(error_message)

    # Each letter of the Roman numeral 
    # is translated into its decimal value
    digits = []
    for letter in number:
        match letter:
            case 'M':
                digits.append(1000)
            case 'D':
                digits.append(500)
            case 'C':
                digits.append(100)
            case 'L':
                digits.append(50)
            case 'X':
                digits.append(10)
            case 'V':
                digits.append(5)
            case 'I':
                digits.append(1)

    # Each value is added (if preceding a smaller or equal one) 
    # or subtracted (if preceded by a larger one)
    number = 0
    size = len(digits)
    for index in range(size):
        if size == index + 1:
            number += digits[index]
        elif digits[index] < digits[index + 1]:
            number -= digits[index]
        else:
            number += digits[index]

    return number