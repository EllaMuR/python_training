import pymysql
from model.group import Group
from model.contact import Contact

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor =  self.connection.cursor()
        try:
            cursor.execute("SELECT group_id, group_name, group_header, group_footer FROM group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

    def get_contact_list(self):
        list = []
        cursor =  self.connection.cursor()
        try:
            cursor.execute("SELECT id, firstname, middlename, lastname, nickname, company, title, address,"
                            "home, mobile, work, email, email2, email3, homepage, bday, bmonth, byear, aday, amonth, ayear "
                           "FROM addressbook")
            for row in cursor:
                (id, firstname, middlename, lastname, nickname, company, title, address, homephone, mobile_phone, work_phone, email1,
                 email2, email3, home_page, bday, bmonth, byear, aday, amonth, ayear ) = row
                list.append(Contact(id=str(id), firstname=firstname, middlename=middlename, lastname=lastname,
                                    nickname=nickname, company=company, title=title, address=address, homephone=homephone,
                                    mobile_phone=mobile_phone, work_phone=work_phone, email1=email1, email2=email2, email3=email3,
                                    home_page=home_page, bday=bday, bmonth=bmonth, byear=byear, aday=aday, amonth=amonth, ayear= ayear))
        finally:
            cursor.close()
        return list