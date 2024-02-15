import pytest
import pytest_html
#from Ques_2 i
import math_operations

@pytest.mark.smoke
def test_add():
    sum = math_operations.add(4,5)
    assert sum == 9
    sum1 = math_operations.add(100,-10)
    assert sum1 == 110


@pytest.mark.smoke
def test_sub():
    sub = math_operations.subtract(10,1)
    assert sub == 1
    sub1 = math_operations.subtract(10000,9987984)
    assert sub1 < 0

@pytest.mark.stress
def test_mul():
    mul = math_operations.multiply(10,200)
    assert mul == 2000
    mul1 = math_operations.multiply(9999,0)
    assert mul1 == 0

@pytest.mark.smoke
def test_div():
    try:
        div = math_operations.divide(10,50)
    except(ValueError):
        assert div == "Value Error"

def pytest_html_report_title(report):
    report.title="q4.html"
