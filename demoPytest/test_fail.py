import pytest

class Test_Math:
    def test_divide_number(self):
        pytest.xfail("need to investigate")
        num = 10
        result = num +num
        assert result == num/num

    @pytest.mark.xfail(reason="Results add numbers & not multiply numbers")
    def test_square_number(self):
        num = 10
        result =num+num
        assert result == num**2

    @pytest.mark.xfail(reason="Results and Assert are correct")
    def test_cube_number(self):
        num = 10
        result =num**3
        assert result == num**3

    @pytest.mark.xfail(run=False)
    def test_number_square(self):
        num = 10
        result =num*num
        assert result == num**2
    

    
