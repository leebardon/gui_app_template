import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(__file__, "..", "..", "..")))
from ldap3 import Server, Connection, ALL
import sys

# You probably shouldn't touch these settings:

AD_SERVER = "ldaps://nlbldap.soton.ac.uk"
AD_MEMBER_ATTRIBUTE = "member"
AD_USERNAME_ATTRIBUTE = "sAMAccountName"

# Settings you might want to change
REALM_DN = "DC=soton,DC=ac,DC=uk"
AD_GROUP_TEMPLATE = "(&(objectClass=user)(memberof=CN=%s,OU=resource,OU=jf,OU=jf,OU=pk,OU=User,DC=soton,DC=ac,DC=uk))"
AD_GROUPS = ['ou=user']

def list_active_users(group):

    try:
        ad = Server(AD_SERVER)
        conn = Connection(ad)
        conn.bind()
    except Exception as ex:
        sys.stderr.write("Unable to connect to LDAP server: " + str(ex) + "\n")
        sys.exit(1)
    else:
        users = list()
        # search for the group
        search_string = AD_GROUP_TEMPLATE
        results =  conn.search(REALM_DN, search_string, attributes=['cn'])
        print(results)
        try:
            for result in results:
                users.append(result[1]["cn"][0])
        except TypeError:
            if results == None:
                sys.stderr.write("Could not find AD group\n")
                sys.exit(1)
            elif type(results) == list:
                pass
            else:
                raise
    return users


def generate_users_list(filename, users):
    FILE_HEADER = "EXTERNAL_COURSE_KEY|EXTERNAL_PERSON_KEY|ROLE|AVAILABLE_IND"
    LINE_PREFIX = "staff|student|Y"
    try:
        with open(filename, "w") as fp:
            fp.write(FILE_HEADER + "\n")
            decoded = [user.decode("utf-8") for user in users]
            for username in decoded:
                    fp.write(LINE_PREFIX + username + "|instructor|Y\n")
    except Exception as ex:
        sys.stderr.write("Unable to write to output file: " + str(ex) + "\n")
        sys.exit(2)


if __name__ == "__main__":
    users = set()
    for ad_group in AD_GROUPS:
        users.update(list_active_users(ad_group))
        print(users)

