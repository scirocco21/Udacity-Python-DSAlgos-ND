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
child.add_user("bob")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

visited_groups = []

def is_user_in_group(user, group):
  for member in group.users:
    if member == user:
      return True
  for member in group.groups:
     # only go through groups that have not been visited
    if member not in visited_groups:
      return is_user_in_group(user,member)
    # if the group doesn't have the user, don't search again
    visited_groups.append(member)
  return None

# print(is_user_in_group("bob", parent))