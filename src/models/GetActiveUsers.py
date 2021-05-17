from ldap3 import Server, Connection, AUTO_BIND_NO_TLS, SUBTREE, ALL_ATTRIBUTES, ALL, DEREF_NEVER
from pathlib import Path
from datetime import date
import sys, os
import json

basepath = Path.cwd()
outdir = os.path.dirname(basepath)
today = str(date.today())

AD_SERVER = "ldaps://nlbldap.soton.ac.uk"
AD_MEMBER_ATTRIBUTE = "member"
AD_USERNAME_ATTRIBUTE = "sAMAccountName":quit

# Settings to return all active users:
OUTPUT_FILE = f"{outdir}/active.users.{today}.out"
REALM_DN = "DC=soton,DC=ac,DC=uk"
AD_GROUP_TEMPLATE = "(&(objectClass=user)(memberof=CN=%s, ou=user, dc=soton, dc=ac, dc=uk))"
AD_GROUPS = ["allStaff_category", "allPGR_category", "allPGT_category", "allUG_category"]



def list_active_users(group):
    try:
        server = Server(AD_SERVER, get_info=ALL)
        conn = Connection(server, auto_bind=True)
    except Exception as ex:
        sys.stderr.write("Unable to connect to LDAP server: " + str(ex) + "\n")
        sys.exit(1)
    else:
        users = list()
        conn.search(REALM_DN, AD_GROUP_TEMPLATE % ad_group)
        entries = conn.extend.standard.paged_search(REALM_DN, AD_GROUP_TEMPLATE % ad_group, attributes=['cn'], paged_size=10)

        try:
            for e in entries:
                if e['type'] == 'searchResEntry':
                    users.append(e['attributes']['cn'][0])
        except TypeError:
            if entries == None:
                sys.stderr.write("Could not find AD group\n")
                sys.exit(1)
            elif type(entries) == list:
                pass
            else:
                raise
    return users


def generate_users_list(filename, users):

    try:
        with open(filename, "w") as fp:
            for username in users:
                fp.write(f"{username}\n")
    except Exception as ex:
        sys.stderr.write("Unable to write to output file: " + str(ex) + "\n")
        sys.exit(2)


if __name__ == "__main__":
    users = set()
    for ad_group in AD_GROUPS:
        users = list_active_users(ad_group)
    generate_users_list(OUTPUT_FILE, users)