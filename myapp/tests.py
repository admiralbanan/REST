# myapp/tests.py

from django.test import TestCase
from .models import Person, CarAccident
from django.utils import timezone

class PersonModelTest(TestCase):

    def setUp(self):
        Person.objects.create(first_name='Иван', last_name='Иванов', age=30)
        Person.objects.create(first_name='Мария', last_name='Петрова', age=25)

    def test_full_name_method(self):
        """Проверка метода get_full_name() модели Person."""
        person = Person.objects.get(first_name='Иван')
        self.assertEqual(person.get_full_name(), 'Иван Иванов')


class CarAccidentModelTest(TestCase):

    def setUp(self):
        self.accident = CarAccident.objects.create(
            brand='Toyota',
            license_plate='А123ВС77',
            year_of_manufacture=2015,
            last_accident_date=timezone.now().date(),
            compensation_amount=50000,
            passengers_injured=False
        )

    def test_str_method(self):
        """Проверка строкового представления модели CarAccident."""
        self.assertEqual(str(self.accident), 'Toyota - А123ВС77')
