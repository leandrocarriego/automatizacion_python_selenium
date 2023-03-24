from selenium.webdriver.common.by import By

class Page_Navigator() :
    def __init__(self, driver) :
        self.driver = driver
         
    def go_to(self, element_to_search) :
        element_to_go = self.driver.find_element(by=By.ID, value=element_to_search)
        element_to_go.click()
        self.driver.implicitly_wait(10)