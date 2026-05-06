"""
Test cases proposed by ChatGPT 4o.

- No new errors are found.
- 1 potential improvement in the code under test is identified: lowercase Roman numerals could be converted to uppercase
- 9 false positives are raised 
"""
import pytest
from app.roman_numerals import roman_to_decimal

# ✅ Valid Roman numeral tests
@pytest.mark.parametrize("roman, expected", [
    ("I", 1),
    ("III", 3),
    ("IV", 4),
    ("IX", 9),
    ("X", 10),
    ("XL", 40),
    ("L", 50),
    ("XC", 90),
    ("C", 100),
    ("CD", 400),
    ("D", 500),
    ("CM", 900),
    ("M", 1000),
    ("MCMXCIV", 1994),
    ("MMMCMXCIX", 3999),
    ("CDXLIV", 444),
    ("MMMDCCCLXXXVIII", 3888),
    ("XXX", 30),
    ("XIV", 14),
    ("xiv", 14),  # Test lowercase normalization
])
def test_valid_roman_numerals(roman, expected):
    assert roman_to_decimal(roman) == expected


# ❌ Invalid Roman numeral tests
@pytest.mark.parametrize("roman", [
    "IIII", "XXXX", "CCCC", "MMMM",       # Excessive repetition
    "VV", "LL", "DD",                    # V, L, D repeated
    "VX", "VL", "VC", "VD", "VM",        # Invalid subtractive combinations
    "LC", "LD", "LM", "DM",              # More invalid orders
    "IC", "IL", "ID", "IM",              # I before invalid numerals
    "ABC", "X#", "M CM", "Ⅸ",            # Invalid characters or Unicode
    "", " ", "X ", "\nX", "X\n",         # Whitespace/formatting issues
    "IVIV",                              # Duplicate subtractive sequences
])
def test_invalid_roman_numerals(roman):
    with pytest.raises(Exception, match="Badly formed Roman numeral"):
        roman_to_decimal(roman)