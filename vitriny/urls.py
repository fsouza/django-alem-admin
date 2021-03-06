from django.conf.urls.defaults import *
from core.models import Product

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^vitriny/', include('vitriny.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    (r'^new_product', 'django.views.generic.create_update.create_object', { 'model' : Product, 'post_save_redirect' : '/products/', 'template_name' : 'product_form.html'}),
    (r'^login/$', 'django.contrib.auth.views.login', { 'template_name' : 'login.html' }),
    (r'^logout/$', 'django.contrib.auth.views.logout', { 'next_page' : '/new_product' }),
    (r'^contact/$', 'core.views.contact'),
    (r'^$', 'core.views.say_hello'),
)
