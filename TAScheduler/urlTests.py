from django.test import TestCase
from django.test import Client



class TestUrls(TestCase):
    def setUp(self):
        self.client=Client()

    def test_loginTemplates(self):
        r = self.client.get("/login/")
        self.assertEqual(r.templates[0].name, "login.html")

    def test_courseCreationTemplates(self):
        r = self.client.get("/coursemanagement/")
        self.assertEqual(r.templates[0].name, "courseManagement.html")

    def test_accountCreationTemplates(self):
        r = self.client.get("/accountmanagement/")
        self.assertEqual(r.templates[0].name,  "accountManagement.html")

    def test_loginPath(self):
        r=self.client.get("/login/")
        self.assertEqual(r.context.request.path, "/login/")

    def test_courseCreationPath(self):
        r=self.client.get("/coursemanagement/")
        self.assertEqual(r.context.request.path, "/coursemanagement/")

    def test_accountCreationPath(self):
        r=self.client.get("/accountmanagement/")
        self.assertEqual(r.context.request.path, "/accountmanagement/")

