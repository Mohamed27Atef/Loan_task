from django.urls import path
from . import views
urlpatterns = [
    path('create/',views.loan_details,name='loan_details'),
]
