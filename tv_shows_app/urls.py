from django.urls import path
from . import views

urlpatterns = [
    path('',views.redirect_to_main_page),
    path('shows',views.display_main_page),
    path('shows/new',views.display_form_to_add_tv_show),
    path('shows/create',views.add_form_data_to_database),
    path('shows/<int:show_id>',views.display_show_information),
    path('shows/<int:show_id>/edit',views.display_form_to_update_show_information),
    path('shows/<int:show_id>/update',views.update_form_information_in_database),
    path('shows/<int:show_id>/destroy',views.delete_show_information_from_database),
]