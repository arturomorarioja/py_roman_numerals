"""
Test cases proposed by ChatGPT 5.5

- The potential improvement in the code under test that it identified last year is no more
- But it identified 3 actual errors whose problem is insufficient requirements
    - Requirements should state that
        - Only one Roman number can precede a bigger one
          (e.g., IV, not IIV; or XD, not XXD)
        - A Roman number can precede the next number, but not skip a level
          (e.g., XC, not XM)
- 19 false positives are raised 
"""
import pytest
from app.roman_numerals import roman_to_decimal


@pytest.mark.parametrize(
    'roman, expected',
    [
        ('I', 1),
        ('V', 5),
        ('X', 10),
        ('L', 50),
        ('C', 100),
        ('D', 500),
        ('M', 1000),
    ]
)
def test_single_roman_figures(roman, expected):
    assert roman_to_decimal(roman) == expected


@pytest.mark.parametrize(
    'roman, expected',
    [
        ('II', 2),
        ('III', 3),
        ('VI', 6),
        ('VII', 7),
        ('VIII', 8),
        ('XI', 11),
        ('XII', 12),
        ('XV', 15),
        ('XX', 20),
        ('XXX', 30),
        ('LX', 60),
        ('CX', 110),
        ('MDCCCLXVII', 1867),
    ]
)
def test_additive_roman_numerals(roman, expected):
    assert roman_to_decimal(roman) == expected


@pytest.mark.parametrize(
    'roman, expected',
    [
        ('IV', 4),
        ('IX', 9),
        ('XL', 40),
        ('XC', 90),
        ('CD', 400),
        ('CM', 900),
        ('XIV', 14),
        ('XIX', 19),
        ('XLIV', 44),
        ('XCIV', 94),
        ('MCMXCIX', 1999),
        ('MMMCMXCIX', 3999),
    ]
)
def test_subtractive_roman_numerals(roman, expected):
    assert roman_to_decimal(roman) == expected


@pytest.mark.parametrize(
    'roman, expected',
    [
        ('MMXXIV', 2024),
        ('MMXXVI', 2026),
        ('CDXLIV', 444),
        ('DCCCXC', 890),
        ('MCDLIII', 1453),
        ('MCMLXXXIV', 1984),
        ('MMCDXXI', 2421),
    ]
)
def test_mixed_valid_roman_numerals(roman, expected):
    assert roman_to_decimal(roman) == expected


@pytest.mark.parametrize(
    'roman',
    [
        '',
        'IIII', 'XXXX', 'CCCC', 'MMMM',     # Excessive repetition
        'VV', 'LL', 'DD',                   # V, L, D repeated
        'IL', 'IC', 'ID', 'IM',             # I before invalid numerals
        'VX',                               # Invalid subtractive combination
        'LC', 'DM',                         # More invalid orders
        'ABC',                              # Invalid characters
        
        # New test cases (not generated in 2025)
        'XD',           # False positive, as it raises an exception
        'MMMMCMXCIX',   # False positive, as it raises an exception
        'MMXXA',        # False positive, as this implementation ignores invalid characters (A)
        'XM',           # ERROR: X can directly precede C, but not M. 990 is CMXC
        'IIV',          # ERROR: Only one I can precede a V. 3 is III
        'XXC',          # ERROR: Only one X can precede a C. 80 is LXXX
    ]
)
def test_invalid_roman_numerals_raise_value_error(roman):
    with pytest.raises(ValueError):
        roman_to_decimal(roman)