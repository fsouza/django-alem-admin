# Create your views here.
from models import Product
from django import forms
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product

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
