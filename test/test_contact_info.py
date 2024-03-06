import re
from model.contact import Contact
from random import randrange

def test_contact_info_on_homepage(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="Тест", middlename="Тестович", lastname="Тестовый",
                                nickname="Test",  homephone="+789456", email1="test1test@test.ru", bday="11",
                                    bmonth="August", byear="2001"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_homepage = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert clear_spaces(contact_from_homepage.lastname) == clear_spaces(contact_from_edit_page.lastname)
    assert clear_spaces(contact_from_homepage.firstname) == clear_spaces(contact_from_edit_page.firstname)
    assert clear(contact_from_homepage.address) == clear(contact_from_edit_page.address)
    assert clear_spaces(contact_from_homepage.all_emails_from_homepage) == merge_emails_like_on_homepage(contact_from_edit_page)
    assert contact_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_edit_page)



# def test_phones_on_contact_view_page(app):
#     old_contacts = app.contact.get_contact_list()
#     index = randrange(len(old_contacts))
#     contact_from_view_page = app.contact.get_contact_from_view_page(index)
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#     assert contact_from_view_page.homephone == contact_from_edit_page.homephone
#     assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
#     assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone


def clear(s):
    return re.sub("[() -]","",s)

def clear_spaces(s):
    return re.sub("[ ]","",s)

def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x!="", map(lambda x: clear(x),
                                                 filter(lambda x: x is not None,
                                                        [contact.homephone, contact.mobile_phone, contact.work_phone]))))

def merge_emails_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x),
                                                   filter(lambda x: x is not None,
                                                          [contact.email1, contact.email2,
                                                           contact.email3]))))
