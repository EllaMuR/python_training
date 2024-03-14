from model.contact import Contact
import random
from random import randrange

def test_delete_some_contact(app, db, check_ui):
    if len(db.get_group_list())==0: #app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="Тест", middlename="Тестович", lastname="Тестовый",
                                nickname="Test", title="test_person", company="test_test",
                                email1="test1test@test.ru", bday="11", bmonth="August", byear="2001"))
    old_contacts = db.get_contact_list()
    #index = randrange(len(old_contacts))
    contact = random.choice(old_contacts)
    #app.contact.delete_by_index(index)
    app.contact.delete_by_id(contact.id)
    new_contacts = db.get_contact_list()
    #assert len(old_contacts) - 1 == len(new_contacts)
    #old_contacts[index:index+1] = []
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts,key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),key=Contact.id_or_max())

