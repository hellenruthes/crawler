from selenium import webdriver
from settings import chrome_drive_path


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(
    executable_path=chrome_drive_path,
    chrome_options=options
    )

path = "/Users/hellenruthes/dev/articles/ieee/"


