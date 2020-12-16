# Active Directory


class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


def return_is_user_in_group(user, group):
    """
    Recursive function to search groups for user.
    :param user: string
    :param group: Group
    :return: True is user is in group. Otherwise, False.
    """
    if user in group.get_users():  # check for user in group list
        # print("IN GROUP:{}".format(group.name))
        return True
    for member in group.get_groups():  # recursion through all group list elements
        # print("Searching group:{}".format(member.name))
        return_is_user_in_group(user, member)
        return False


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    return return_is_user_in_group(user, group)


print(is_user_in_group(sub_child_user, parent))
print(is_user_in_group(sub_child_user, child))
print(is_user_in_group(sub_child_user, sub_child))
