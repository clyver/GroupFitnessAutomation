__author__ = 'ChrisLyver'
from secrets import Secrets
from datetime import datetime
import time


class DailyBookings():
    """
    Northeastern Group Fitness Classes are first come first serve, let's beat the line!
    Each day of the week maps to a certain booking.
    :param driver: A selenium webdriver object authenticated by a user's credentials
                   (see secrets.py) at the NU Group Fitness reservations page.
    """

    def __init__(self, driver):
        self.browser = driver

    def book_a_class(self, class_to_book):
        """
        Find and click the link specified by 'class_to_book'.  Confirm to finalize.
        :param class_to_book: The XPATH to the class link
        """

        time.sleep(3)
        link_to_book = self.browser.find_element_by_xpath(class_to_book)
        link_to_book.click()

        self.confirm()

    def confirm(self):
        """
        We've made our selection.  Confirm and quit the driver.
        """

        time.sleep(3)
        add_appointment = self.browser.find_element_by_xpath('//*[@id="submitButton"]')
        add_appointment.click()

        self.browser.quit()


def get_day_of_week():
    """
    Use datetime lib to get the current day of the week
    :return: An int representation of the day of the week, where 0 is Monday
    """

    this_day = datetime.today().weekday()
    return this_day


def determine_which_class_to_book(current_day):
    """
    Booking begins 24 hours in advance. Ex. For Wednesday classes, we book Tuesday at 12am.
    :param current_day: The current day of the week as an int, per datetime convention in where Monday is 0.
    :return: The XPATH to the link of the class we would like to book.
    """

    # A dict whose key (day of the week) corresponds to the XPATH to the class I want to take that day:
    classes_by_day = {0: '//*[@id="scheduleDisplay"]/table/tbody/tr[36]/td[3]/a',
                      1: '//*[@id="scheduleDisplay"]/table/tbody/tr[19]/td[3]/a',
                      2: '//*[@id="scheduleDisplay"]/table/tbody/tr[37]/td[3]/a[1]',
                      3: "TODO",
                      4: "TODO",
                      5: "TODO",
                      6: "TODO"}
    return classes_by_day.get(current_day + 1)

if __name__ == "__main__":
    # Get the current day
    today = get_day_of_week()
    # Return tomorrow's desired class, based on today's day
    desired_class = determine_which_class_to_book(today)
    # Start up our session
    my_credentials = Secrets()
    browser = my_credentials.web_login()
    # Instantiate, and book the desired class
    bookings = DailyBookings(browser)
    bookings.book_a_class(desired_class)