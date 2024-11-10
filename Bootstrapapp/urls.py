from django.urls import path
from Bootstrapapp import views


urlpatterns=[
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('why/',views.why,name='why'),
    path('testimonial/',views.testimonial,name='testimonial'),
    path('shop/',views.shop,name='shop'),

]