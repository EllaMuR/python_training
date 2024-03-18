from model.group import Group
from model.contact import Contact
import random
from fixture.orm import ORMFixture

database = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_add_contact_to_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if len(db.get_group_list()) == 0:
        app.contact.add_new(Contact(firstname="Тест", middlename="Тестович", lastname="Тестовый",
                                nickname="Test", title="test_person", company="test_test",
                                email1="test1test@test.ru", bday="11", bmonth="August", byear="2001"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    old_contacts_in_group = database.get_contacts_in_group(Group(id=group.id))
    contacts_not_in_group = database.get_contacts_not_in_group(Group(id=group.id))
    if len(contacts_not_in_group) == 0:
        app.contact.add_new(Contact(firstname="Test_contact", lastname="test_lastname"))
    contacts_not_in_group = database.get_contacts_not_in_group(Group(id=group.id))
    contact = random.choice(contacts_not_in_group)
    app.contact.add_contact_to_group(contact.id, group.id)
    new_contacts_in_group = database.get_contacts_in_group(group)
    assert len(old_contacts_in_group) + 1 == len(new_contacts_in_group)
