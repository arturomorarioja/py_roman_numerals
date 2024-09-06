import pytest
from app.roman_numerals import roman_to_decimal

@pytest.mark.parametrize('roman_number,decimal_number', [
    ('', 0),                # Valid lower boundary
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
    ('MMMCMXCIX', 3999)     # Valid upper boundary
])
def test_roman_numerals_passes(roman_number, decimal_number):
    assert roman_to_decimal(roman_number) == decimal_number

@pytest.mark.parametrize('roman_number', [
    ('MXDIVII'),
    ('VV'),
    ('MDVVI'),
    ('MDVXVI'),
    ('LL'),
    ('MDLLX'),
    ('MDLXLV'),
    ('DD'),
    ('MDDCX'),
    ('MDCDXVI'),
    ('IIII'),
    ('XVIIII'),
    ('CLIIIIX'),
    ('XXXX'),
    ('MDXXXX'),
    ('MCXXXXV'),
    ('CCCC'),
    ('MDCCCC'),
    ('MCCCCDV'),
    ('MMMM'),        # Invalid upper boundary
    ('MMMMCL'),
    ('DM'),
    ('LM'),
    ('LD'),
    ('LC'),
    ('VM'),
    ('VD'),
    ('VC'),
    ('VL'),
    ('VX'),
    ('XD'),
    ('IM'),
    ('ID'),
    ('IC'),
    ('IL')
])
def test_badly_formed_roman_numerals(roman_number):
    with pytest.raises(Exception):
        roman_to_decimal(roman_number)