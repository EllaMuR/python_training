from model.contact import Contact
from random import randrange

def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="Тест", middlename="Тестович", lastname="Тестовый",
                                nickname="Test", title="test_person", company="test_test",
                                email1="test1test@test.ru", bday="11", bmonth="August", byear="2001"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts

