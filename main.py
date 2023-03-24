import unittest
import HtmlTestRunner
from selenium import webdriver
from pages.Page_Navigator import *
from pages.Page_Complete_Form import *

class TestLoginForm(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./resources/webDriver/chromedriver.exe")
        print("INCICIANDO...")
        self.driver.get("https://www.consultoriaglobal.com.ar/")
        self.driver.implicitly_wait(10)
        print("MAXIMIZAR VENTANA")
        self.driver.maximize_window()
        
    def test_email_validation(self):
        # Navega a la seccion de contacto
        print("CLICK PARA IR A LA SECCION DE CONTACTO")
        navigator = Page_Navigator(self.driver)
        navigator.go_to("menu-item-1364")

        # Se completa el formulario
        autocomplete_form = Page_Complete_Form(self.driver)
        autocomplete_form.complete_form("Leandro", "lean@emailfalso.com", "test", "1234")
        autocomplete_form.submit_form()
        self.assertEqual(autocomplete_form.value_of_email(), True, "EL EMAIL INGRESADO SE DETECTO COMO 'INVALIDO'")
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="reports"))