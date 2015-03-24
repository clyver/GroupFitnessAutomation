__author__ = 'Chris1'
from secrets import Secrets
from datetime import datetime

# Login to NU Group Fitness and hand-off the state of the browser


class DailyBookings():
    """
    Northeastern Group Fitness Classes are first come first serve, let's beat the line!
    Each day of the week maps to a certain booking.
    :param driver: A selenium webdriver object authenticated by a user's credentials
                   (see secrets.py) at the NU Group Fitness reservations page.
    """

    def __init__(self, driver):
        self.browser = driver

    def monday(self):
        """
        Book the 7:05pm 'crank it up' class
        """

        crank_it_up = self.browser.find_element_by_xpath('//*[@id="scheduleDisplay"]/table/tbody/tr[36]/td[3]/a')
        crank_it_up.click()

        self.confirm()

    def tuesday(self):
        """
        Book the 8:15pm 'cycle' class
        """

        cycle_class = self.browser.find_element_by_xpath('//*[@id="scheduleDisplay"]/table/tbody/tr[19]/td[3]/a')
        cycle_class.click()

        self.confirm()

    def wednesday(self):
        """
        Book the 7:!0 'cycle' class
        """

        cycle_class = self.browser.find_element_by_xpath('//*[@id="scheduleDisplay"]/table/tbody/tr[37]/td[3]/a[1]')
        cycle_class.click()

        self.confirm()

    def thursday(self):
        pass

    def friday(self):
        pass

    def saturday(self):
        pass

    def sunday(self):
        pass

    def confirm(self):
        """
        We've made our selection.  Confirm and quit the driver.
        """
        add_apointment = self.browser.find_element_by_xpath('//*[@id="submitButton"]')
        add_apointment.click()

        self.browser.quit()


def get_day_of_week():
    """
    Use datetime lib to get the current day of the week
    :return: An int representation of the day of the week, where 0 is Monday
    """

    this_day = datetime.today().weekday()
    return this_day


def determine_which_day_to_book(current_day):
    """
    Booking begins 24 hours in advance. Ex. For Wednesday classes, we book Tuesday at 12am.
    :param current_day: The current day of the week as an int, per datetime convention in where Monday is 0.
    :return: The day we would like to book, as a string.
    """

    days_of_the_week = {0: "monday",
                        1: "tuesday",
                        2: "wednesday",
                        3: "thursday",
                        4: "friday",
                        5: "saturday",
                        6: "sunday"}
    return days_of_the_week.get(current_day + 1)

if __name__ == "__main__":
    # Get the current day
    today = get_day_of_week()
    # Return tomorrow's name as a string
    to_book = determine_which_day_to_book(today)
    # Start up our session
    my_credentials = Secrets()
    browser = my_credentials.web_login()
    bookings = DailyBookings(browser)
    # Get the appropriate function to call
    reserve = getattr(bookings, to_book)
    # Reserve our spot in the class and get buff
    reserve()