import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(__file__, "..", "..", "..")))

from src.models import GetActiveUsers, Save


def get_active_ldap_users():

    users = GetActiveUsers.get_users()
    Save.generate_users_list(users[0])


if __name__ == "__main__":
    get_active_ldap_users()
