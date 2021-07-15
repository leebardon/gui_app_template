from ldap3 import Server, Connection, ALL

# from src.models import Save
from pathlib import Path
from datetime import date
import numpy as np
import sys, os
import json


class Vars:
    pass


_v = Vars()
_v.TODAY = str(date.today())
_v.BASEPATH = Path.cwd()
_v.OUTDIR = os.path.dirname(_v.BASEPATH)
_v.PARENT = f"{_v.OUTDIR}/H&S Incomplete Courses/"


class ServerSettings:
    pass


_s = ServerSettings()
_s.AD_SERVER = "ldaps://nlbldap.soton.ac.uk"
_s.MEMBER_ATTRIBUTE = "member"
_s.USERNAME_ATTRIBUTE = "sAMAccountName"


# Settings to return all active users:
REALM_DN = "DC=soton,DC=ac,DC=uk"
AD_GROUP_TEMPLATE = (
    "(&(objectClass=user)(memberof=CN=%s, ou=user, dc=soton, dc=ac, dc=uk))"
)
AD_GROUPS = [
    "allStaff_category",
    "allPGT_category",
    "allUG_category",
]


def get_users():
    users = []
    for ad_group in AD_GROUPS:
        users.append(list_active_users(ad_group))
    all_users = np.concatenate((users[0], users[1], users[2]))
    return all_users


def list_active_users(ad_group):
    try:
        server = Server(_s.AD_SERVER, get_info=ALL)
        conn = Connection(server, auto_bind=True)
    except Exception as ex:
        sys.stderr.write("Unable to connect to LDAP server: " + str(ex) + "\n")
        sys.exit(1)
    else:
        users = list()
        conn.search(REALM_DN, AD_GROUP_TEMPLATE % ad_group)
        entries = conn.extend.standard.paged_search(
            REALM_DN, AD_GROUP_TEMPLATE % ad_group, attributes=["cn"], paged_size=10
        )

        try:
            for e in entries:
                if e["type"] == "searchResEntry":
                    users.append(e["attributes"]["cn"][0])
        except TypeError:
            if entries == None:
                sys.stderr.write("Could not find AD group\n")
                sys.exit(1)
            elif type(entries) == list:
                pass
            else:
                raise
    return users


if __name__ == "__main__":
    get_users()
