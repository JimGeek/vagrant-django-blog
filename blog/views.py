from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
	context = RequestContext(request)
	context_dict = {'message': "Nest is sold to google for $2.9B"}
	return render_to_response('blog/index.html',context_dict,context)

def aboutus(request):
	context = RequestContext(request)
	context_dict = {}
	return render_to_response('blog/aboutus.html',context_dict,context)
