from baidu_page import BaiduPage
import unittest
from time import sleep
from selenium import webdriver
from parameterized import parameterized

class TestBaidu(unittest.TestCase):
    """百度搜搜测试"""

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(r'd:\python\chromedriver.exe')
        cls.base_url = "http://www.baidu.com"

    def test_baidu_search_case1(self):
        self.driver.get(self.base_url)
        bd = BaiduPage(self.driver)
        bd.search_input("selenium")
        bd.search_button()

    def test_baidu_search_case2(self):
        self.driver.get(self.base_url)
        bd = BaiduPage(self.driver)
        bd.search_input("unittest")
        bd.search_button()

    def test_baidu_search_case3(self):
        self.driver.get(self.base_url)
        bd = BaiduPage(self.driver)
        bd.search_input("page object")
        bd.search_button()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
