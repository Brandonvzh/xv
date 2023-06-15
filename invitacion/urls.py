from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from invitacion import views

app_name = "invitacion"

urlpatterns = [
    path("home/guests/", views.table_guests, name = "table-guests"),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
