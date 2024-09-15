from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from medical.models import Service, Doctor
from users.models import User, Record


class TestService(TestCase):
    """ Тестирование сервиса """

    def setUp(self):
        self.service = Service.objects.create(name="TEST1",
                                              description="Прием терапевта",
                                              price=1000.00)
        self.user = User.objects.create(email='test@example.com')
        self.doctor = Doctor.objects.create(name="Мария",
                                            surname="Крылова",
                                            patronymic="Витальевна",
                                            job_title="Врач-терапевт", )
        self.record = Record.objects.create(user=self.user,
                                            service=self.service,
                                            doctor=self.doctor,
                                            record_time="2024-09-16")
        self.client = Client()
        self.list_url = reverse('medical:home')
        self.create_url = reverse('medical:create')
        self.detail_url = reverse('medical:service_detail', args=[self.service.pk])

    def test_create_service(self):
        """ Тестирование создания сервиса """

        response = self.client.post(self.create_url, {"name": "TEST2",
                                                      "description": "УЗИ",
                                                      "price": '1000.00', })

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(Service.objects.all().count(), 1)
        self.assertEqual(self.service.name, "TEST1")

    def test_list_service(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'medical/home.html')

    def test_detail_service(self):
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_delete_service(self):
        """ Тестирование удаления сервиса """

        url = reverse("medical:delete", args=(self.service.pk,))
        data = {
            "name": "TEST1",
            "description": "Прием терапевта",
            "price": '10000.00',
        }

        response = self.client.delete(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_edit_service(self):
        """ Тестирование изменения сервиса """

        url = reverse("medical:edit", args=(self.service.pk,))
        data = {
            "name": "TEST2",
            "description": "УЗИ",
            "price": '1000.00',
        }

        response = self.client.put(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(data.get("name"), "TEST2")
        self.assertEqual(data.get("description"), "УЗИ")
        self.assertEqual(data.get("price"), '1000.00')


class TestRecord(TestCase):
    """ Тестирование записи """

    def setUp(self):
        self.service = Service.objects.create(name="TEST1",
                                              description="Прием терапевта",
                                              price=1000.00)
        self.user = User.objects.create(email='test1@example.com')
        self.doctor = Doctor.objects.create(name="Мария",
                                            surname="Крылова",
                                            patronymic="Витальевна",
                                            job_title="Врач-терапевт",)
        self.record = Record.objects.create(user=self.user,
                                            service=self.service,
                                            doctor=self.doctor,
                                            record_time="2024-09-16")
        self.client = Client()
        self.list_url = reverse('users:record_list')
        self.create_url = reverse('users:record')

    def test_create_record(self):
        """ Тестирование создания записи """

        data = {
            "user": self.user,
            "service": self.service,
            "doctor": self.doctor,
            "record_time": "2024-09-16"
        }
        response = self.client.post(self.create_url, data=data)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(Record.objects.all().count(), 1)
        self.assertEqual(self.record.user.email, 'test1@example.com')
        self.assertEqual(self.record.service.name, "TEST1")

    def test_list_record(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'users/record_list.html')

    def test_delete_record(self):
        """ Тестирование удаления записи """

        url = reverse("users:record_delete", args=(self.record.pk,))
        data = {
            "user": self.user,
            "service": self.service,
            "doctor": self.doctor,
            "record_time": "2024-09-16"
        }

        response = self.client.delete(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_edit_record(self):
        """ Тестирование изменения записи """

        url = reverse("users:record_edit", args=(self.record.pk,))
        doctor = Doctor.objects.create(name="Елена",
                                            surname="Иванова",
                                            patronymic="Вадимовна",
                                            job_title="Врач-уролог",)

        data = {
            "user": self.user,
            "service": self.service,
            "doctor": doctor,
            "record_time": "2024-09-16"
        }

        response = self.client.put(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(Record.objects.all().count(), 1)
        self.assertEqual(self.record.user.email, 'test1@example.com')
        self.assertEqual(self.record.service.name, "TEST1")

