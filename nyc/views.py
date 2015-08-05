from django.shortcuts import render
from .models import Person, Bill, Organization, Action

def index(request):
	recent_legislation = Bill.objects.order_by('date_updated')[:10]
	context = {
		'recent_legislation': recent_legislation
	}

	return render(request, 'nyc/index.html', context)

def bill_detail(request, bill_id):

	legislation = Bill.objects.filter(ocd_id=bill_id).first()

	context={
		'legislation': legislation
	}

	return render(request, 'nyc/legislation.html', context)

def committees(request):

	committees = Organization.committees()
	print committees

	context={
		'committees': committees
	}

	return render(request, 'nyc/committees.html', context)