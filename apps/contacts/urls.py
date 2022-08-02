from django.urls import path, include

from . import views

app_name = "contacts"

urlpatterns = [
    path("", views.ContactsShowView.as_view(), name="show_contacts"),
    path("create_contact", views.ContactCreateView.as_view(), name="create_contact"),
    path(
        "<int:pk>/",
        include(
            [
                path("show_contact_info", views.ContactInfoShowView.as_view(), name="show_contact_info"),
                path("update_contact", views.ContactUpdateView.as_view(), name="update_contact"),
                path("delete_contact", views.ContactDeleteView.as_view(), name="delete_contact"),
            ]
        ),
    ),
]
