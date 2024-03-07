# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
import random
import string
import re


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + " "*10 + string.digits # + string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone_number(prefix, maxlen):
     numbers = string.digits+" "+"-"
     return prefix + "".join([random.choice(numbers) for i in range(random.randrange(maxlen))])



testdata = [Contact(firstname="",middlename="",lastname="")] + [
      Contact(firstname=random_string("firstname",20),
              middlename=random_string("middlename",20),
              lastname=random_string("lastname",20),
              title=random_string("title",30),
              company=random_string("company",30),
              address=random_string("address",100),
              homephone=random_phone_number("+",9),
              mobile_phone=random_phone_number("",12),
              work_phone=random_string("wphone",12),
              email1=random_string("email1",30),
              email2=random_string("email2",30),
              email3=random_string("email3",30),
              home_page=random_string("home_page",50),
              bday = str(random.randrange(1,31)),
              bmonth = random.choice(["January","February","March","April","May","June","July",
                                      "August","September","October","November","December"]),
              byear = random_string("",4),
              aday = str(random.randrange(1,31)),
              amonth = random.choice(["January","February","March","April","May","June","July",
                                      "August","September","October","November","December"]),
              ayear = random_string("",4))
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    # contact = Contact(firstname="Григорий", middlename="Евгеньевич", lastname="Врублевский",
    #                             nickname="Hunter", title="person", company="MBQwerty",
    #                             address="Нижний Новгород, улица Советская, дом 5", homephone="+7888999999",
    #                             mobile_phone="+79819999999", work_phone="+7888777777", email1="hunter1@test.ru",
    #                             email2="gr.evg.vr@test.ru", home_page="google.com", bday="12", bmonth="May", byear="1999",
    #                             aday="12", amonth="May", ayear="2024")
    app.contact.add_new(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def clear_spaces(s):
    return re.sub("[ ]","",s)


