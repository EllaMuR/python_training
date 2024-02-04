from model.contact import Contact

def test_modify_first_contact(app):
    app.contact.modify_first_contact(Contact(firstname="Вероника", middlename="Петрова", lastname="Евгеньевна",
    nickname="Verona", title="person2", company="MBQwerty",
    address="Город, улица, дом", homephone="+7888999991",
    mobile_phone="+79819999991", work_phone="+7888777771", email1="verona1@test.ru",
    email2="", home_page="google.com", bday="26", bmonth="November", byear="1999",
    aday="11", amonth="April", ayear="2023"))



