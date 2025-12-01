import pytest


# @pytest.mark.skip(reason="Demonstrate how to skip a class")
# @pytest.mark.xfail(reason="Demonstrate how to XFAIL/XPASS a class")
class Test_Math:

    # @pytest.mark.xfail(run=False)
    # Pass
    def test_number_square(self):
        num = 10
        result =num*num
        assert result == num**2

    def test_divide_number(self):
        # pytest.xfail("need to investigate")
        # Fail
        num = 10
        result = num + num
        assert result == num/num

    # @pytest.mark.xfail(reason="Results add numbers & not multiply numbers")
    # Fail
    def test_square_number(self):
        num = 10
        result =num+num
        assert result == num**2

    # @pytest.mark.xfail(reason="Results and Assert are correct")
    # Pass
    def test_cube_number(self):
        num = 10
        result =num**3
        assert result == num**3


    

    
