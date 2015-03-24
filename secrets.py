__author__ = 'Chris1'
from selenium import webdriver


class Secrets():
    """
    This class uses the selenium webdriver to login to Northeastern University's
    Group Fitness portal.  To do so you must already be signed up and have an
    active username and password.
    """
    def __init__(self):
        self.login = "<your-username>"
        self.password = "<your-password>"

    def web_login(self):
        """
        Login and navigate to the "Register For Class" page.
        :return: An active selenium webdriver object positioned at the class listings.
        """
        browser = webdriver.Firefox()
        browser.get('https://nucampusrec.cshape.net/memberLogin.aspx')

        username = browser.find_element_by_name('txtUser')
        username.send_keys(self.login)

        password = browser.find_element_by_name('txtPassword')
        password.send_keys(self.password)

        login = browser.find_element_by_name('signInButton')
        login.click()

        register_for_class = browser.find_element_by_xpath('//*[@id="regClassesLink"]')
        register_for_class.click()

        return browser