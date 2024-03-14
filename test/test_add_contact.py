# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.db import DbFixture
import re


#@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, json_contacts, db, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    # contact = Contact(firstname="Григорий", middlename="Евгеньевич", lastname="Врублевский",
    #                             nickname="Hunter", title="person", company="MBQwerty",
    #                             address="Нижний Новгород, улица Советская, дом 5", homephone="+7888999999",
    #                             mobile_phone="+79819999999", work_phone="+7888777777", email1="hunter1@test.ru",
    #                             email2="gr.evg.vr@test.ru", home_page="google.com", bday="12", bmonth="May", byear="1999",
    #                             aday="12", amonth="May", ayear="2024")
    app.contact.add_new(contact)
    #assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts,key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),key=Contact.id_or_max())

# def clear_spaces(s):
#     return re.sub("[ ]","",s)


