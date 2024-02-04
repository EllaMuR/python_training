from model.group import Group


def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test", footer="test"))
    app.group.modify_first_group(Group(name="modified_group", header="other_header", footer="other_footer"))


def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test", footer="test"))
    app.group.modify_first_group(Group(name="New_group"))

def test_modify_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test", footer="test"))
    app.group.modify_first_group(Group(header="New_header"))

def test_modify_first_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test", footer="test"))
    app.group.modify_first_group(Group(header="New_footer"))