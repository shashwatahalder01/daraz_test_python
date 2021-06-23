from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException


# this Base class is serving basic attributes for every single page inherited from Page class
class BasePage(object):
    
    def __init__(self, driver, base_url="about:blank"):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 90

    # Interacting with the page_________________________

    # Find single element
    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    # Find multiple elements
    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    # Clear input field
    def clear_input_field(self, *locator):
        self.find_element(*locator).send_keys(Keys.CONTROL + 'a')
        self.find_element(*locator).send_keys(Keys.DELETE)

    # or

    def clear_field(self, *locator):
        self.find_element(*locator).clear()

    # Clear input field and then send data to input field
    def clear_input_field_and_send_keys(self, data, *locator):
        self.find_element(*locator).send_keys(Keys.CONTROL + 'a')
        self.find_element(*locator).send_keys(Keys.DELETE)
        self.find_element(*locator).send_keys(data)

    # Get title of the url
    def get_title(self):
        return self.driver.title

    # Mouse hover on an element
    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    # Filling in forms_________________________________

    # Select 'Select' element by index value
    def select_by_index(self, index, *locator):
        select = Select(self.driver.find_element(*locator))
        return select.select_by_index(index)

    # Select 'Select' element by visible text
    def select_by_visible_text(self, text, *locator):
        select = Select(self.find_element(*locator))
        return select.select_by_visible_text(text)

    # Select 'Select' element by value
    def select_by_value(self, value, *locator):
        select = Select(self.driver.find_element(*locator))
        return select.select_by_value(value)

    # De-select all 'Select' element
    def deselect_all(self, * locator):
        select = Select(self.driver.find_element(*locator))
        select.deselect_all()

    # Get list of all default selected options
    def get_selected_options(self, * locator):
        select = Select(self.driver.find_element(*locator))
        all_selected_options = select.all_selected_options
        return all_selected_options

    # Get list of all options
    def get_all_options(self, * locator):
        select = Select(self.driver.find_element(*locator))
        options = select.options
        return options

    # Submit form
    def submit_form(self, *locator):
        element = self.find_element(*locator)
        element.submit()

    # Drag and drop______________________________________

    # Drag and drop an element
    def drag_and_drop(self, source_locator, target_locator):
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        drag_and_drop = ActionChains(self.driver).drag_and_drop(source, target)
        drag_and_drop.perform()

    # Moving between windows and frames____________________

    # Switch to window
    def switch_to_window(self, window):
        return self.driver.switch_to_window(window)

    # Switch to frame or iframe
    def switch_to_frame(self, frame):
        return self.driver.switch_to_frame(frame)

    # Switch to sub_frame or iframe
    def switch_to_sub_frame(self, parent_frame, child_frame):
        return self.driver.switch_to_frame(parent_frame + '.' + child_frame)

    # Switch to parent window
    def switch_to_parent_window(self):
        return self.driver.switch_to_default_content()

    # Popup dialogs______________________________________

    # Switch to alert
    def switch_to_alert(self):
        return self.driver.switch_to.alert

    #  Navigation _______________________________________

    # Open desired url
    def open_url(self, url):
        self.driver.get(url)

    # Open sub_url of main domain
    def open_sub_url(self, url):
        #  Base url is the main domain
        url = self.base_url + url
        self.driver.get(url)

    # Get current page url
    def get_url(self):
        return self.driver.current_url

    # Refresh page
    def refresh(self):
        return self.driver.refresh()

    # Go to forward page
    def go_forward(self):
        return self.driver.forward()

    # Go back to previous page
    def go_back(self):
        return self.driver.back()

    #  Cookies ___________________________________________

    # Set cookie for the entire domain
    def set_cookies(self, url, name, value):
        cookie = {'name': name, 'value': value}
        self.driver.get(url)
        self.driver.add_cookie(cookie)

    # Get all the available cookies for the current URL
    def get_cookies(self, url):
        self.driver.get(url)
        self.driver.get_cookies()

    # Waits__________________________________________________

    # Explicit wait

    #  title is

    # title contains

    #  wait till presence of element is located
    def wait_till_presence_of_element_located(self, seconds, *locator):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(EC.presence_of_element_located(*locator))
        return element

    #  wait till visibility_of_element_located
    def wait_till_visibility_of_element_located(self, seconds, *locator):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(EC.visibility_of_element_located(*locator))
        return element

    # visibility of

    #  wait till presence_of_all_elements_located
    def wait_till_presence_of_all_elements_located(self, seconds, *locator):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(EC.presence_of_all_elements_located(*locator))
        return element

    #  wait till text_to_be_present_in_element
    def wait_till_text_to_be_present_in_element(self, seconds, *locator):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(EC.text_to_be_present_in_element(*locator))
        return element

    #  wait till text_to_be_present_in_element_value
    def wait_till_text_to_be_present_in_element_value(self, seconds, *locator):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(EC.text_to_be_present_in_element_value(*locator))
        return element

    #  wait till frame_to_be_available_and_switch_to_it
    def wait_till_frame_to_be_available_and_switch_to_it(self, seconds, *locator):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(EC.frame_to_be_available_and_switch_to_it(*locator))
        return element

    #  wait till invisibility_of_element_located
    def wait_till_invisibility_of_element_located(self, seconds, *locator):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(EC.invisibility_of_element_located(*locator))
        return element

    #  wait till element_to_be_clickable
    def wait_till_element_to_be_clickable(self, seconds, *locator):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(EC.element_to_be_clickable(*locator))
        return element
    # staleness of

    #  wait till element_to_be_selected
    def wait_till_element_to_be_selected(self, seconds, *locator):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(EC.element_to_be_selected(*locator))
        return element

    #  wait till element_located_to_be_selected
    def wait_till_element_located_to_be_selected(self, seconds, *locator):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(EC.element_located_to_be_selected(*locator))
        return element

    #  wait till element_selection_state_to_be
    def wait_till_element_selection_state_to_be(self, seconds, *locator):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(EC.element_selection_state_to_be(*locator))
        return element

    #  wait till element_located_selection_state_to_be
    def wait_till_element_located_selection_state_to_be(self, seconds, *locator):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(EC.element_located_selection_state_to_be(*locator))
        return element

    #  wait till alert_is_present
    def wait_till_alert_is_present(self, seconds):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(EC.alert_is_present)
        return element
    # custom wait

    # implicit wait
    def implicit_waits(self, seconds):
        return self.driver.implicitly_wait(seconds)

    # def assert_true(self, result):
    #     assert result is True
    #
    # def assert_false(self, result):
    #     assert result is False
    #
    # def assert_in(self, result, data):
    #     assert result in data
    #
    # def assert_not_in(self, result, data):
    #     assert result not in data

    # self.assertEqual()
    # self.assertEquals()
    # self.assertTrue()
    # self.assertFalse()
    # self.assert_()
    # self.assertAlmostEqual()
    # self.assertAlmostEquals()
    # self.assertNotAlmostEqual()
    # self.assertNotAlmostEquals()
    # self.assertCountEqual()
    # self.assertDictEqual()
    # self.assertGreater()
    # self.assertGreaterEqual()
    # self.assertIn()
    # self.assertIs()
    # self.assertIsNot()
    # self.assertIsNone()
    # self.assertIsNotNone()
    # self.assertIsInstance()
    # self.assertNotIsInstance()
    # self.assertLess()
    # self.assertLessEqual()
    # self.assertListEqual()
    # self.assertLogs()
    # self.assertMultiLineEqual()

    # def wait_element(self, *locator):
    #     try:
    #         WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
    #     except TimeoutException:
    #         print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" %(locator[1]))
    #         self.driver.quit()

    # def wait_element1(self, *locator):
    #     try:
    #         ignored_exceptions = (NoSuchElementException, StaleElementReferenceException )
    #         WebDriverWait(self.driver, 10, ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located(locator))
    #     except TimeoutException:
    #         print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" %(locator[1]))
    #         self.driver.quit()

    # dynamic locator
    #     def symptom(name):
    #         typename = f"//span[contains(text(), '{name}')]"
    #         return typename

    # ID = "id"
    # XPATH = "xpath"
    # LINK_TEXT = "link text"
    # PARTIAL_LINK_TEXT = "partial link text"
    # NAME = "name"
    # TAG_NAME = "tag name"
    # CLASS_NAME = "class name"
    # CSS_SELECTOR = "css selector"

    # use try catch instead of if else
    # clear input field first

    # Keys.RETURN  Keys.ARROW_DOWN
