from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)
n=5
f="data/contacts.json"

for o, a in opts:
    if o=="-n":
        n=int(a)
    elif o=="-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10 #+ string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone_number(prefix, maxlen):
    numbers = string.digits + " " + "-"
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

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file,"w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))