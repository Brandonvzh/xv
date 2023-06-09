from django.urls import path
from invitacion import views

app_name = "invitacion"

urlpatterns = [
    path("home/guests/", views.table_guests, name = "table-guests"),
]
