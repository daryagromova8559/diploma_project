from django.urls import path
from django.views.decorators.cache import cache_page

from medical.apps import MedicalConfig
from medical.views import ServiceCreateView, ServiceListView, ServiceUpdateView, contacts, company, mission, \
    ServiceDeleteView, ServiceDetailView, DoctorCreateView, DoctorListView, DoctorUpdateView, DoctorDeleteView, \
    DoctorDetailView

app_name = MedicalConfig.name


urlpatterns = [
    path('create/', ServiceCreateView.as_view(), name='create'),
    path('', ServiceListView.as_view(), name='home'),
    path('edit/<int:pk>/', ServiceUpdateView.as_view(), name='edit'),
    path('contact/', cache_page(60)(contacts), name='contact'),
    path('company/', cache_page(60)(company), name='company'),
    path('mission/', cache_page(60)(mission), name='mission'),
    path('delete/<int:pk>/', ServiceDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
    path('doctors_create/', DoctorCreateView.as_view(), name='doctors_create'),
    path('doctors_list', DoctorListView.as_view(), name='doctors_list'),
    path('doctors_edit/<int:pk>/', DoctorUpdateView.as_view(), name='doctors_edit'),
    path('doctors_delete/<int:pk>/', DoctorDeleteView.as_view(), name='doctors_delete'),
    path('doctor_detail/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
]