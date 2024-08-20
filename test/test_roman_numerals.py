import pytest
from app.roman_numerals import roman_to_decimal

@pytest.mark.parametrize('roman_number,decimal_number', [
    ('', 0),            
    ('M', 1000),            
    ('MD', 1500),            
    ('MCD', 1400),
    ('MDCCCLXVII', 1867),
    ('XCIV', 94),
    ('CCC', 300),
    ('I', 1),
    ('X', 10),
    ('IX', 9),
    ('MMXXIII', 2023),
    ('MMJXXOIII', 2023),
    ('MXDIVII', 1496),
])
def test_roman_numerals(roman_number, decimal_number):
    assert roman_to_decimal(roman_number) == decimal_number