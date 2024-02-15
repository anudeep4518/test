import pytest
import logging
from selenium import webdriver
import pytest_html
import q3

class Test_triangle():
    @pytest.fixture
    def setup(self):
        self.logger = logging.getLogger()
        t1 = q3.triangle()
        self.logger.info("web page opened")
        return t1

    def tear_down(self,setup):
        del setup
        del self.logger

    def test_iso(self,setup):
        self.logger.info("testing for an isoseles traingle")
        res = setup.trian(1,2,2)
        assert res == "Isosceles"
        self.logger.info("testing completed")

    def test_equ(self,setup):
        self.logger.info("testing for an Equilateral traingle")
        res = setup.trian(2,2,2)
        assert res == "Equilateral"
        self.logger.info("testing for Equilateral traingle completed")

    def test_scal(self,setup):
        self.logger.info("testing for an Scalene traingle")
        res = setup.trian(5,6,2)
        assert res == "Scalene"
        self.logger.info("testing for an Scalene traingle completed")

    def test_nat(self,setup):
        self.logger.info("testing for an Not a triangle")
        res = setup.trian(1,2,1)
        assert res == "Error: Not a Triangle"
        self.logger.info("testing for an not a traingle is completed")




def pytest_html_report_title(report):
    report.title="q4.html"