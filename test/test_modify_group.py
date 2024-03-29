from model.group import Group
from random import randrange


def test_modify_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = (Group(name="modified_group", header="other_header", footer="other_footer"))
    group.id = old_groups[index].id
    #app.group.modify_group_by_index(index, group)
    app.group.modify_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


# def test_modify_group_name(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test", header="test", footer="test"))
#     old_groups = app.group.get_group_list()
#     index = randrange(len(old_groups))
#     group = (Group(name="New_group"))
#     group.id = old_groups[index].id
#     app.group.modify_group_by_index(index, group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#     old_groups[index] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def test_modify_first_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test", header="test", footer="test"))
#     app.group.modify_first_group(Group(header="New_header"))
#
# def test_modify_first_group_footer(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test", header="test", footer="test"))
#     app.group.modify_first_group(Group(header="New_footer"))