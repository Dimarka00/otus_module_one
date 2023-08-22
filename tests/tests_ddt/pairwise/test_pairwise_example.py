import pytest
from allpairspy import AllPairs


class TestParametrized:
    @pytest.mark.parametrize('brand, operating_system, browser', [
        value_list for value_list in AllPairs([
            ['DELL', 'ACER', 'ASUS'],
            ['WIN7', 'XP', 'WIN10'],
            ['CHROME', 'FIREFOX', 'IE11']
        ])
    ])
    def test_with_pw(self, brand, operating_system, browser):
        pass
