import re
from model.contact import Contact
from random import randrange


def test_match_contact_info_on_homepage_and_db(app, db):
    if len(db.get_group_list()) == 0:
        app.contact.add_new(Contact(firstname="Тест", middlename="Тестович", lastname="Тестовый",
                                    nickname="Test", title="test_person", company="test_test",
                                    email1="test1test@test.ru", bday="11", bmonth="August", byear="2001"))
    #db_contacts = db.get_contact_list()
    contact_from_homepage = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    l = len(db.get_contact_list())
    for i in range(l):
    #index = randrange(len(db_contacts))
    # contact_from_homepage = app.contact.get_contact_list()[index]
    # contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
        assert contact_from_homepage[i].lastname == replace_many_spaces(contacts_from_db[i].lastname)
        assert contact_from_homepage[i].firstname == replace_many_spaces(contacts_from_db[i].firstname)
        assert contact_from_homepage[i].address == replace_many_spaces(contacts_from_db[i].address)
        assert clear_spaces(contact_from_homepage[i].all_emails_from_homepage) == merge_emails_like_on_homepage(contacts_from_db[i])
        assert contact_from_homepage[i].all_phones_from_homepage == merge_phones_like_on_homepage(contacts_from_db[i])


# def test_contact_info_on_homepage(app):
#     if app.contact.count() == 0:
#         app.contact.add_new(Contact(firstname="Тест", middlename="Тестович", lastname="Тестовый",
#                                 nickname="Test",  homephone="+789456", email1="test1test@test.ru", bday="11",
#                                     bmonth="August", byear="2001"))
#     old_contacts = app.contact.get_contact_list()
#     index = randrange(len(old_contacts))
#     contact_from_homepage = app.contact.get_contact_list()[index]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#     assert contact_from_homepage.lastname == replace_many_spaces(contact_from_edit_page.lastname)
#     assert contact_from_homepage.firstname == replace_many_spaces(contact_from_edit_page.firstname)
#     assert contact_from_homepage.address == replace_many_spaces(contact_from_edit_page.address)
#     assert clear_spaces(contact_from_homepage.all_emails_from_homepage) == merge_emails_like_on_homepage(contact_from_edit_page)
#     assert contact_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_edit_page)



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
    return re.sub(" ","",s)

def replace_many_spaces(s):
    return re.sub(" +", " ", s)


def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x!="", map(lambda x: clear(x),
                                                 filter(lambda x: x is not None,
                                                        [contact.homephone, contact.mobile_phone, contact.work_phone]))))

def merge_emails_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x),
                                                   filter(lambda x: x is not None,
                                                          [contact.email1, contact.email2,
                                                           contact.email3]))))
