from model.contact import Contact
from random import randrange
import random

def test_modify_contact(app, db, check_ui):
    if len(db.get_group_list())==0:
        app.contact.add_new(Contact(firstname="Тест", middlename="Тестович", lastname="Тестовый",
                                nickname="Test", title="test_person", company="test_test",
                                email1="test1test@test.ru", bday="11", bmonth="August", byear="2001"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    #select_contact = random.choice(old_contacts)
    contact = Contact( firstname="Вероника", middlename="Петрова", lastname="Евгеньевна",
    nickname="Verona", title="person2", company="MBQwerty",
    address="Город, улица, дом", homephone="+7888999991",
    mobile_phone="+79819999991", work_phone="+7888777771", email1="verona1@test.ru",
    email2="", home_page="google.com", bday="26", bmonth="November", byear="1999",
    aday="11", amonth="April", ayear="2023")
    contact.id = old_contacts[index].id
    #contact.id = select_contact.id
    #app.contact.modify_contact_by_index(index, contact)
    app.contact.modify_contact_by_id(contact.id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


# def test_modify_first_contact_fio(app):
#     if app.contact.count() == 0:
#         app.contact.add_new(Contact(firstname="Тест", middlename="Тестович", lastname="Тестовый",
#                                 nickname="Test", title="test_person", company="test_test",
#                                 email1="test1test@test.ru", bday="11", bmonth="August", byear="2001"))
#     old_contacts = app.contact.get_contact_list()
#     index = randrange(len(old_contacts))
#     contact = Contact(firstname="Проверка", middlename="Проверочная", lastname="Тестовая")
#     contact.id = old_contacts[index].id
#     app.contact.modify_contact_by_index(index, contact)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#     old_contacts[index] = contact
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_modify_first_contact_email(app):
#     if app.contact.count() == 0:
#         app.contact.add_new(Contact(firstname="Тест", middlename="Тестович", lastname="Тестовый",
#                                 nickname="Test", title="test_person", company="test_test",
#                                 email1="test1test@test.ru", bday="11", bmonth="August", byear="2001"))
#     app.contact.modify_first_contact(Contact(email1="testtest1@test.ru"))
#
# def test_modify_first_contact_bdate(app):
#     if app.contact.count() == 0:
#         app.contact.add_new(Contact(firstname="Тест", middlename="Тестович", lastname="Тестовый",
#                                 nickname="Test", title="test_person", company="test_test",
#                                 email1="test1test@test.ru", bday="11", bmonth="August", byear="2001"))
#     app.contact.modify_first_contact(Contact(bday="19", bmonth="June", byear="1992"))
