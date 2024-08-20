def roman_to_decimal(number: str) -> int:

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