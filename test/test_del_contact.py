from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="Тест", middlename="Тестович", lastname="Тестовый",
                                nickname="Test", title="test_person", company="test_test",
                                email1="test1test@test.ru", bday="11", bmonth="August", byear="2001"))
    app.contact.delete_first()

