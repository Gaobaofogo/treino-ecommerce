# coding=utf-8

from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Category
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View, TemplateView, CreateView
from django.contrib.auth import get_user_model
from django.contrib import messages

from .forms import ContactForm

User = get_user_model()

class IndexView(TemplateView):

	template_name = 'index.html'


index = IndexView.as_view()

def contact(request):
	success = False
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form.envio_de_email()
		success = True
		form = ContactForm()
	elif request.method == 'POST':
		messages.error(request, 'Formulário inválido')
	context = {
		'form': form,
		'success': success,
	}
	return render(request, 'contact.html', context)