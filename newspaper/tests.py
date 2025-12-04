from django.test import TestCase
from django.urls import reverse

from accounts.models import Redactor
from newspaper.models import Newspaper, Topic


class NewspaperTests(TestCase):
    def setUp(self):
        # Підготовка даних перед кожним тестом
        self.topic = Topic.objects.create(name="IT News")
        self.redactor = Redactor.objects.create_user(
            username="testuser", password="password123", years_of_experience=5
        )
        self.newspaper = Newspaper.objects.create(
            title="Django Testing",
            content="Automated tests are cool.",
            topic=self.topic
        )
        self.newspaper.publishers.add(self.redactor)

    def test_newspaper_content(self):
        # Перевірка, чи правильно збереглися дані в БД
        news = Newspaper.objects.get(id=self.newspaper.id)
        self.assertEqual(news.title, "Django Testing")
        self.assertEqual(news.topic.name, "IT News")

    def test_homepage_status_code(self):
        # Перевірка, чи відкривається головна сторінка (код 200)
        response = self.client.get(reverse("newspaper:index"))
        self.assertEqual(response.status_code, 200)
