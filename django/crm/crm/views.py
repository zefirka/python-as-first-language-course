from django.http import HttpResponse

import datetime

import crm.model.model as crm

def index(request):
    return HttpResponse(crm.all())

def customer(request, name):
	return HttpResponse(crm.get_customer(name))

def new_customer(request, name):
	crm.create.customer(name)
	return HttpResponse('New customer {0} created'.format(name))

def buy(request, customer_name, product):	
	return HttpResponse(crm.buy(customer_name, product))

def products(request):
	return HttpResponse(crm.get_all_products())