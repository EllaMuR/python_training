from sys import maxsize


class Contact:
    def __init__(self,firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, homephone=None, mobile_phone=None, work_phone=None, all_phones_from_homepage=None,
                 email1=None, email2=None, email3=None, all_emails_from_homepage = None,
                 home_page=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None, ayear=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.all_phones_from_homepage = all_phones_from_homepage
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.all_emails_from_homepage = all_emails_from_homepage
        self.home_page = home_page
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
