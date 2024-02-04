from model.group import Group


def test_modify_first_group(app):
    app.group.modify_first_group(Group(name="modified_group", header="other_header", footer="other_footer"))


def test_modify_first_group_name(app):
    app.group.modify_first_group(Group(name="New_group"))

def test_modify_first_group_header(app):
    app.group.modify_first_group(Group(header="New_header"))