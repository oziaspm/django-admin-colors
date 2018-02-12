from admincolors.context_processors import admin_theme
from django.test import RequestFactory
from django.test import TestCase


class TestContextProcessors(TestCase):

    def setUp(self):
        self.request = RequestFactory().get('/admin/')
        self.request.COOKIES['theme'] = 'test.css'

    def test_admin_theme(self):
        context = admin_theme(self.request)
        self.assertEqual(context, {
            'theme': 'test.css'
        })
