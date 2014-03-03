'''Tests for nuit'''
# pylint: disable=R0904
from django.test import TestCase
from django.test.utils import override_settings
from ..context_processors import nuit as nuit_context_processor

class NuitContextProcessors(TestCase):
    '''Tests Nuit's context processors'''

    sample_settings = {
        'NUIT_APPLICATIONS': [{'name': 'Link', 'link': 'http://www.google.com'}],
        'NUIT_GLOBAL_TITLE': 'Title',
        'NUIT_LARGE_LOGO': 'logo.png',
        'NUIT_SMALL_LOGO': 'small_logo.png',
    }

    def test_nuit_context_processor(self):
        with self.settings(**self.sample_settings):
            resulting_dict = nuit_context_processor(None)
        self.assertEqual(resulting_dict, self.sample_settings)

class NuitHandlers(TestCase):
    '''Tests Nuit's handlers'''
    urls = 'nuit.tests.urls'

    @override_settings(COMPRESS_OFFLINE=False)
    def test_error_400(self):
        response = self.client.get('/error400/')
        self.assertEqual(response.status_code, 400)

    @override_settings(COMPRESS_OFFLINE=False)
    def test_error_403(self):
        response = self.client.get('/error403/')
        self.assertEqual(response.status_code, 403)

    @override_settings(COMPRESS_OFFLINE=False)
    def test_error_404(self):
        response = self.client.get('/error404/')
        self.assertEqual(response.status_code, 404)

    @override_settings(COMPRESS_OFFLINE=False)
    def test_error_500(self):
        response = self.client.get('/error500/')
        self.assertEqual(response.status_code, 500)
