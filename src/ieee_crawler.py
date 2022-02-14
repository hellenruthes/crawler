from selenium import webdriver
from settings import chrome_drive_path
import time


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(
    executable_path=chrome_drive_path,
    chrome_options=options
    )

#driver.get('https://www-periodicos-capes-gov-br.ez48.periodicos.capes.gov.br/index.php?')
time.sleep(10)


#driver.get('https://www-periodicos-capes-gov-br.ez48.periodicos.capes.gov.br/index.php/acesso-cafe.html')
#driver.get('https://shibboleth.utfpr.edu.br/idp/profile/SAML2/Redirect/SSO?execution=e2s1')
driver.get('https://www-periodicos-capes-gov-br.ezl.periodicos.capes.gov.br/index.php/acesso-cafe.html')
time.sleep(30)
instituicao = driver.find_element_by_id("select2-listaInstituicoesCafe-container")

instituicao.send_keys("utfpr")
#password.send_keys("Pa55worD")

#driver.find_element_by_name("submit").click()