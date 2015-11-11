"""
WSGI config for lulu project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lulu.settings")

#application = get_wsgi_application()

#import os
import sys
import site
root =os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0,root)

packages = os.path.join(root,'lulu.today/lib/python2.7/site-packages')
sys.path.insert(0,packages)

#add the site-packages of the chosen virtualenv to work with
site.addsitedir(packages)
#add the app's directory to the PYTHONPATH
sys.path.append('/home/Lulu/lulu')
sys.path.append('/home/Lulu/lulu/lulu')
#add side packages for virtual envs
#sys.path.append('/.virtualenvs/Lib/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'lulu.settings'


#Activate your virtual env
activate_env = os.path.join(root,'lulu.today/bin/activate_this.py')

execfile(activate_env, dict(__file__ = activate_env))
#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
