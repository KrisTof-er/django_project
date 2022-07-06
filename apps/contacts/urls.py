from django.urls import path, include

from . import views

app_name = 'contacts'

urlpatterns = [
    path('', views.show_contacts, name="show_contacts"),
    path('create_contact', views.create_contact, name="create_contact"),
    path('<int:pk>/', include([
        path('show_contact_info', views.show_contact_info, name="show_contact_info"),
        path('update_contact', views.update_contact, name="update_contact"),
        path('delete_contact', views.delete_contact, name="delete_contact"),
    ])),
]
