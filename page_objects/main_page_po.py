class MainPagePO:
    def __init__(self, driver):
        self.driver = driver

    def get_logo_image(self):
        return self.driver.find_element_by_css_selector('img[src="https://www.dbserver.com.br/images/LogoDB.png"]')
