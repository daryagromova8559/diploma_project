from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

from medical.forms import ServiceForm, DoctorForm
from medical.models import Service, Doctor
from users.services import get_qs_from_cache


class ServiceListView(ListView):
    model = Service
    template_name = 'medical/home.html'


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'У вас новое сообщение: {name}({phone}): {message}')
    return render(request, 'medical/contacts.html')


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'У вас новое сообщение: {name}({phone}): {message}')
    return render(request, 'medical/home_page.html')


def company(request):
    return render(request, 'medical/company.html')


def mission(request):
    return render(request, 'medical/mission.html')


class ServiceCreateView(LoginRequiredMixin, CreateView):
    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy('medical:home')
    login_url = "users:login"
    redirect_field_name = "redirect_to"


class ServiceUpdateView(LoginRequiredMixin, UpdateView):
    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy('medical:home')
    login_url = "users:login"
    redirect_field_name = "redirect_to"


class ServiceDeleteView(LoginRequiredMixin, DeleteView):
    model = Service
    success_url = reverse_lazy('medical:home')
    login_url = "users:login"
    redirect_field_name = "redirect_to"


class ServiceDetailView(LoginRequiredMixin, DetailView):
    model = Service
    template_name = 'medical/service_detail.html'
    login_url = "users:login"
    redirect_field_name = "redirect_to"


class DoctorListView(ListView):
    model = Doctor
    template_name = 'medical/doctors_list.html'

    def get_queryset(self):
        return get_qs_from_cache(qs=Doctor.objects.all(), key='doctor_list')


class DoctorCreateView(LoginRequiredMixin, CreateView):
    model = Doctor
    form_class = DoctorForm
    success_url = reverse_lazy('medical:doctors_list')
    login_url = "users:login"
    redirect_field_name = "redirect_to"


class DoctorUpdateView(LoginRequiredMixin, UpdateView):
    model = Doctor
    form_class = DoctorForm
    success_url = reverse_lazy('medical:doctors_list')
    login_url = "users:login"
    redirect_field_name = "redirect_to"


class DoctorDeleteView(LoginRequiredMixin, DeleteView):
    model = Doctor
    success_url = reverse_lazy('medical:doctors_list')
    login_url = "users:login"
    redirect_field_name = "redirect_to"


class DoctorDetailView(LoginRequiredMixin, DetailView):
    model = Doctor
    template_name = 'medical/doctor_detail.html'
    login_url = "users:login"
    redirect_field_name = "redirect_to"



