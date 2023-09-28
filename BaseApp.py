def find_element(self, locator, times=10):
    return WebDriverWait(self.driver, times).until(EC.presence_of_element_located(locator), message="Не найден эл-т")
    return WebDriverWait(self.driver, times).until(EC.presence_of_element_located(locator), message="Элемент не найден")


def get_element_property(self, locator, property):
    element = self.find_element(locator)