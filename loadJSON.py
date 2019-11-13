import django
from django.conf import settings
from nbaStat.nbaStat.settings import DATABASES, INSTALLED_APPS
settings.configure(DATABASES=DATABASES, INSTALLED_APPS=INSTALLED_APPS)
django.setup()
import json
import sys
from pprint import pprint as pp
from nbaStat.player.models import player

print("got here")
if(len(sys.argv) == 2):
    print("opening file..")
    j = open(sys.argv[1], 'r')
    file = j.read()
    file = json.loads(file)
    for players in file:
        fn = players['first_name']
        ln = players['last_name']
        full = players['full_name']
        id = players['id']
        active = players['is_active']
        p = player(first_name = fn, last_name = ln, full_name = full, id = id, is_active = active)
        p.save()
        print(p)

else:
    print("too many arguments")
