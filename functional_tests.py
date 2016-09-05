from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://iron-classifier.herokuapp.com/')
        self.assertIn('Babel', self.browser.title)
        button = self.browser.find_element_by_id('this_is_the_predict_button')
        button.click()
        search_input = self.browser.find_element_by_name('text_to_classif')
        search_input.send_keys('hello world' + Keys.RETURN)
        self.driver.getPageSource().contains("english")


if __name__ == '__main__':
    unittest.main(warnings='ignore')
