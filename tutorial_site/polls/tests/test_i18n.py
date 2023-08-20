# this is django's test file


from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
# import django http test client
from django.test import Client


class I18NTest(TestCase):
    def test_zh(self):
        client = Client()
        response = client.get(reverse("polls:trans", args=["zh"]))
        self.assertEqual(response.status_code, 200)
        print(response.content.decode("utf-8"))

    def test_en(self):
        client = Client()
        response = client.get(reverse("polls:trans", args=["en"]))
        self.assertEqual(response.status_code, 200)
        print(response.content.decode("utf-8"))

    def test_get_zh_from_http_request(self):
        client = Client()
        # HTTP_ACCEPT_LANGUAGE = "zh"
        resource = response = client.get(reverse("polls:trans", args=["zx"]), headers={"HTTP_ACCEPT_LANGUAGE": "zh"})
        self.assertEqual(response.status_code, 200)
        print(response.content.decode("utf-8"))
