from django.shortcuts import render, redirect

from . import maps, dataprocessing

from .forms import ContactForm
from .models import Message

MY_DEBUG = False

# Create your views here.

def index(request):
	"""The main dashboard"""
	if MY_DEBUG:
		return render(request, 'dashboard/index.html', {'countries': [["Test",100,100,100]],'big_case_num': '100,000','world_map': "Map goes here"})

	data = dataprocessing.world_map_data()

	countries = dataprocessing.left_table(data[0])
	world_map = maps.world_map(data[0])

	context = {
	   'countries': countries,
	   'big_case_num': data[1],
	   'world_map': world_map
	}
	return render(request, 'dashboard/index.html', context)

def page(request):
	#Contact page
	if(request.path == "/contact"):
		if request.method == 'GET':
			form = ContactForm()
		else:
			form = ContactForm(request.POST)
			if form.is_valid():
				subject = form.cleaned_data['subject']
				from_email = form.cleaned_data['from_email']
				message = form.cleaned_data['message']
				msg = Message(email=from_email, subject=subject, message=message)
				msg.save()
				return redirect('/success')
		return render(request, "dashboard/contact.html", {'form': form})
	
	#Anything else
	return render(request, 'dashboard/' + request.path + '.html')