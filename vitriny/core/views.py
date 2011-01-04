# Create your views here.
from models import Product
from django import forms
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.localflavor.br.forms import BRCPFField

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product

class ContactForm(forms.Form):
    name = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=75)
    cpf = BRCPFField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        msg = "Hi, I'm %(name)s. My message for you: %(message)s. My CPF is %(cpf)s." % self.cleaned_data
        send_mail('Subject', '', self.cleaned_data['email'], ['dest@gmail.com'], fail_silently=True)

def new_product(request):
    """Renders a product form on GET requests and
    saves a product on POST requests"""
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Product saved.')
    return render_to_response('product_form.html', {
            'form' : form
        }, context_instance=RequestContext(request)
    )

def contact(request):
    """Renders a contact form on GET requests and
    sends an email on POST requests"""
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return HttpResponse("Mail sent.")
    return render_to_response('contact_form.html', {
            'form' : form
        }, context_instance=RequestContext(request)
    )

@login_required
def say_hello(request):
    """Says Hello world on GET requests"""
    return HttpResponse('Hello world!')
