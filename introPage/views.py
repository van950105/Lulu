from django.shortcuts import render,render_to_response,RequestContext
import MySQLdb
from django.db import connection,transaction
# Create your views here.

def leaveContactInfo(request):
    if 'name' in request.GET:
        db = MySQLdb.connect(user='root', db='lulu_db', passwd='lulutoday', host='localhost')
        name = request.GET['name']
        email = request.GET['email']
        hearFrom = request.GET['hearFrom']
        comments = request.GET['comment']
        cursor = connection.cursor()
        cursor.execute('INSERT INTO introPage_interestinfo(name,email,hearFrom,comments) VALUES (%s,%s,%s,%s)',[name,email,hearFrom,comments])
        #print name,email,hearFrom,comment
        transaction.commit()
        cursor.execute('SELECT name FROM introPage_interestinfo')
        #test = cursor.fetchall()
        #print test
        db.close()
    return render_to_response('introPage.html',context_instance=RequestContext(request))

