# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Григорий", middlename="Евгеньевич", lastname="Врублевский",
                                nickname="Hunter", title="person", company="MBQwerty",
                                address="Нижний Новгород, улица Советская, дом 5", homephone="+7888999999",
                                mobile_phone="+79819999999", work_phone="+7888777777", email1="hunter1@test.ru",
                                email2="gr.evg.vr@test.ru", home_page="google.com", bday="12", bmonth="May", byear="1999",
                                aday="12", amonth="May", ayear="2024")
    app.contact.add_new(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


