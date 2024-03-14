import pymysql
from fixture.db import DbFixture
from fixture.orm import ORMFixture
from model.group import Group

#connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")
db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

# try:
#     groups=db.get_group_list()
#     for group in groups:
#         print(group)
#     print(len(groups))
#
# finally:
#     db.destroy()
#
# try:
#     contacts=db.get_contact_list()
#     for contact in contacts:
#         print(contact)
#     print(len(contacts))
#
# finally:
#     db.destroy()

# try:
#     l = db.get_contact_list()
#     for item in l:
#         print(item)
#     print(len(l))
# finally:
#         pass
try:
    l = db.get_contacts_not_in_group(Group(id='65'))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass


# try:
#     cursor = connection.cursor()
#     cursor.execute("SELECT * FROM group_list")
#     for row in cursor.fetchall():
#         print(row)
# finally:
#     connection.close()