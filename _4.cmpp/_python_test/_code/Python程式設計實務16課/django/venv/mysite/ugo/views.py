# encoding: utf-8
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from datetime import datetime
from django.template.loader import get_template
from ugo.models import urlist

def index(request):
	template = get_template('index.html')
	now = datetime.now
	html = template.render(locals())
	return HttpResponse(html)

def listall(request):
	template = get_template('listall.html')
	all = urlist.objects.all()
	now = datetime.now
	html = template.render(locals())
	return HttpResponse(html)

def gourl(request, short_url):
	try:
		rec = urlist.objects.get(short_url = short_url)
		target_url = rec.src_url
		rec.count = rec.count + 1
		rec.save()
	except:
		target_url = '/notfound/' + short_url
	return redirect(target_url)

def notfound(request, id):
	template = get_template('notfound.html')
	now = datetime.now
	html = template.render({'id':id, 'now': now})
	return HttpResponse(html)