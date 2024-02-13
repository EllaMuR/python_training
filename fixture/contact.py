from selenium.webdriver.support.ui import Select
from model.contact import Contact

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

    def delete_first(self):
        wd = self.app.wd
        self.app.go_to_homepage()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        #wd.SwitchTo().alert().accept()
        #wd.switch_to().alert()
        #wd.switch_to.alert.accept()
        self.app.go_to_homepage()

    def modify_first_contact(self,new_contact_info):
        wd = self.app.wd
        self.app.go_to_homepage()
        # open edit page
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # filling the form
        self.fill_contact_form(new_contact_info)
        # Submit edition
        wd.find_element_by_name("update").click()
        self.app.go_to_homepage()



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

    def get_contact_list(self):
        wd = self.app.wd
        self.app.go_to_homepage()
        contacts = []
        for element in wd.find_elements_by_name(name="entry"):
            text1 = element.find_element_by_css_selector("td:nth-child(3)").text
            text2 = element.find_element_by_css_selector("td:nth-child(2)").text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(firstname=text1, lastname=text2, id=id))
        return contacts