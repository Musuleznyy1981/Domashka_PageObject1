import time

import pytest
from testpage import OperationHelper

username = "Maxim1980"
password = "1d80d84ff6"


def test_step_1(browser):
    test_page1 = OperationHelper(browser)
    test_page1.go_to_site()
    test_page1.enter_login("Maxim1980")
    test_page1.enter_pswd("1d80d84ff6")
    test_page1.click_button()
    time.sleep(3)

    test_page1.click_contact()
    time.sleep(3)

    test_page1.enter_cont_name("Maxim")
    test_page1.enter_cont_email("maksim.musuleznyy@mail.ru")
    test_page1.enter_cont_text("Hi, how are you?")
    time.sleep(1)

    test_page1.click_button()
    time.sleep(1)

    assert test_page1.get_alert_text() == "Form successfully submitted"