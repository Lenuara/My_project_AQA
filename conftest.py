from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
#  драйвер будет открываться и закрываться в каждом тесте (scope='function')
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
# после завершения теста браузер закроется
    yield driver
    driver.quit()