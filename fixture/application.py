# noinspection PyInterpreter
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
#       self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)


    def open_homepage(self):
        wd = self.wd
        if not (wd.current_url.endswith("/addressbook") and len(wd.find_elements_by_xpath("//input[@value='Login']")) > 0):
            wd.get("http://localhost/addressbook/")


    def go_to_homepage(self):
        wd = self.wd
        if not (wd.current_url.endswith("/addressbook") and len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']"))>0):
            wd.find_element_by_link_text("home").click()

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
