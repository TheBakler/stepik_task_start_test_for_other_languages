from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest

class TestMaiPage:

    def test_the_add_to_basket_button_exists(self, browser):
        browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
        wait = WebDriverWait(browser, 10)
        button = wait.until(EC.element_to_be_clickable(browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')))
        assert button.is_displayed(), f"Button not visible!"

if __name__ == '__main__':
    pytest.main()