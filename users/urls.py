from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import UserCreateView, email_confirm, GeneratePasswordView, RecordCreateView, \
    RecordListView, RecordDeleteView, RecordUpdateView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('email_confirm/<str:token>/', email_confirm, name='email_confirm'),
    path('reset_password/', GeneratePasswordView.as_view(template_name='reset_password.html'),
         name='reset_password'),
    path('record/', RecordCreateView.as_view(), name='record'),
    path('record/list/', RecordListView.as_view(), name='record_list'),
    path('record/delete/<int:pk>/', RecordDeleteView.as_view(), name='record_delete'),
    path('record/edit/<int:pk>/', RecordUpdateView.as_view(), name='record_edit'),
]
