from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_new(self, contact):
        wd = self.app.wd
        # init adding a contact
        wd.find_element_by_link_text("add new").click()
        # filling the form
        self.fill_contact_form(contact)
        # submit adding a contact
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        self.app.go_to_homepage()
        self.contact_cache = None

    def select_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_by_index(self, index):
        wd = self.app.wd
        self.app.go_to_homepage()
        self.select_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.app.go_to_homepage()
        self.contact_cache = None

    def delete_first(self):
        self.delete_by_index(0)


    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def open_edit_page(self,index):
        wd = self.app.wd
        #self.app.go_to_homepage()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def open_view_page_by_index(self,index):
        wd = self.app.wd
        #self.app.go_to_homepage()
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()



    def modify_contact_by_index(self, index, new_contact_info):
        wd = self.app.wd
        self.app.go_to_homepage()
        # open edit page of random contact
        self.open_edit_page(index)
        # filling the form
        self.fill_contact_form(new_contact_info)
        # Submit edition
        wd.find_element_by_name("update").click()
        self.app.go_to_homepage()
        self.contact_cache = None


    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname",contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("email", contact.email1)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("homepage", contact.home_page)
        self.select_field_value("bday", contact.bday)
        self.select_field_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.select_field_value("aday", contact.aday)
        self.select_field_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)


    def select_field_value(self, field_value, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(field_value).click()
            Select(wd.find_element_by_name(field_value)).select_by_visible_text(value)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.app.go_to_homepage()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.go_to_homepage()
            self.contact_cache = []
            for element in wd.find_elements_by_name(name="entry"):
                text1 = element.find_element_by_css_selector("td:nth-child(3)").text
                text2 = element.find_element_by_css_selector("td:nth-child(2)").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = element.find_element_by_css_selector("td:nth-child(6)").text.splitlines()
                self.contact_cache.append(Contact(firstname=text1, lastname=text2, id=id, homephone=all_phones[0],
                                                  mobile_phone=all_phones[1], work_phone=all_phones[2]))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self,index):
        wd = self.app.wd
        self.app.go_to_homepage()
        #self.select_by_index(index)
        self.open_edit_page(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, mobile_phone=mobile_phone, work_phone=work_phone)

    def get_contact_from_view_page(self,index):
        wd = self.app.wd
        self.app.go_to_homepage()
        self.open_view_page_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)",text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        return Contact(homephone=homephone, mobile_phone=mobile_phone,
                       work_phone=work_phone)


