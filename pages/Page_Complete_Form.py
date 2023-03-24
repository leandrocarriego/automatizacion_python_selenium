from selenium.webdriver.common.by import By

class Page_Complete_Form():
    def __init__(self, driver):
        self.driver = driver

    def complete_form(self, name, email, subject, captcha):
        # Se seleccionan los campos del formulario
        name_input = self.driver.find_element(by=By.NAME, value="your-name")
        email_input = self.driver.find_element(by=By.NAME, value="your-email")
        subject_input = self.driver.find_element(by=By.NAME, value="your-subject")
        captcha_input = self.driver.find_element(by=By.NAME, value="captcha-636")

        # Se completan los campos del formulario
        print("SE INGRESAN DATOS EN EL INPUT 'NOMBRE'")
        name_input.send_keys(name)
        
        print("SE INGRESAN DATOS EN EL INPUT 'EMAIL'")
        email_input.send_keys(email)
        
        print("SE INGRESAN DATOS EN EL INPUT 'ASUNTO'")
        subject_input.send_keys(subject)

        print("SE INGRESAN DATOS EN EL INPUT 'CAPTCHA'")
        captcha_input.send_keys(captcha)

        self.driver.implicitly_wait(10)

    def submit_form(self):
        # Se hace click en el boton para enviar el formulario
        submit_button = self.driver.find_element(by=By.XPATH, value="//input[@class='wpcf7-form-control wpcf7-submit'][@type='submit']")
        print("SE HACE CLICK EN 'ENVIAR'")
        submit_button.click()
        self.driver.implicitly_wait(10)

    def value_of_email(self):
        # Se retorna un boolean si el email es valido o no
        value_email = self.driver.find_element(by=By.NAME, value="your-email").get_attribute("aria-invalid")
        return bool(value_email)
        