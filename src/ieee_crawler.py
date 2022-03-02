import time
import logging
from selenium import webdriver
from settings import chrome_drive_path
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


def _main():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(
        executable_path=chrome_drive_path,
        chrome_options=options
        )

    sleeping_and_logging(3)

    driver.get('https://www-periodicos-capes-gov-br.ezl.periodicos.capes.gov.br/index.php/acesso-cafe.html')
    sleeping_and_logging(2)
    
    logging.warning("Looking for element id select2-selection__rendered and clicking on it")
    driver.find_element_by_class_name('select2-selection__rendered').click()
    sleeping_and_logging(1)

    logging.warning("Writing university name")
    driver.find_element_by_class_name('select2-search__field').send_keys("UTFPR - UNIVERSIDADE TECNOLOGICA FEDERAL DO PARANA")
    driver.find_element_by_class_name('select2-search__field').send_keys(Keys.RETURN)
    sleeping_and_logging(1)
    
    driver.find_element_by_id('enviarInstituicaoCafe').click()
    sleeping_and_logging(4)


def sleeping_and_logging(time_in_seconds):
    logging.warning("Sleeping for {} second(s)...".format(time_in_seconds))
    time.sleep(time_in_seconds)
    

_main()