import time
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from settings import chrome_drive_path, university_name, cafe_url


def _log_on_cafe():

    driver = return_driver(chrome_drive_path)

    sleeping_and_logging(3)

    driver.get(cafe_url)

    sleeping_and_logging(2)

    logging.warning(
        "Looking for element id select2-selection__rendered and clicking on it"
        )
    driver.find_element_by_class_name(
        'select2-selection__rendered'
        ).click()
    sleeping_and_logging(1)

    logging.warning("Writing university name")
    driver.find_element_by_class_name('select2-search__field') \
        .send_keys(university_name)
    driver.find_element_by_class_name('select2-search__field') \
        .send_keys(Keys.RETURN)
    sleeping_and_logging(1)
    driver.find_element_by_id('enviarInstituicaoCafe').click()
    sleeping_and_logging(4)


def return_driver(chrome_drive_path):
    try:
        print("Inside try")
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(
            executable_path=chrome_drive_path,
            chrome_options=options
            )
        return driver
    except Exception:
        logging.error("Not able to get driver")


def sleeping_and_logging(time_in_seconds):
    logging.warning("Sleeping for {} second(s)...".format(time_in_seconds))
    time.sleep(time_in_seconds)


_log_on_cafe()
