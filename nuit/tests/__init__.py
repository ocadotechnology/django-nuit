'''Tests for nuit'''
# pylint: disable=R0904
import re
from django.test import TestCase
from django.test.utils import override_settings
from django.contrib.messages import constants

from ..context_processors import nuit as nuit_context_processor
from ..templatetags.nuit import message_class, message_icon, set_active_menu, menu_item, calculate_widths

from BeautifulSoup import BeautifulSoup as soup

class NuitContextProcessors(TestCase):
    '''Tests Nuit's context processors'''

    sample_settings = {
        'NUIT_APPLICATIONS': [{'name': 'Link', 'link': 'http://www.google.com'}],
        'NUIT_GLOBAL_TITLE': 'Title',
        'NUIT_GLOBAL_LINK': 'http://www.google.com',
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

class FakeMessage(object):
    def __init__(self, level):
        self.level = level

class NuitTemplateFilters(TestCase):
    '''Tests Nuit's template filters'''

    def test_message_class(self):
        self.assertEqual('alert', message_class(FakeMessage(constants.ERROR)))
        self.assertEqual('info', message_class(FakeMessage(constants.INFO)))

    def test_message_icon(self):
        self.assertEqual('star', message_icon(FakeMessage(constants.INFO)))

def re_search(needle, haystack):
    return re.search(r'\b%s\b' % needle, haystack)

class NuitTemplateTags(TestCase):
    '''Tests Nuit's template tags'''

    def test_set_active_menu(self):
        output = soup(set_active_menu('bob')).find('span')
        self.assertEqual('bob', output.text)
        self.assertEqual('nuit-active-menu', dict(output.attrs)['class'])
        self.assertEqual('display: none', dict(output.attrs)['style'])

    def test_menu_item(self):
        output = soup(menu_item(link='/', name='bob')).find('li')
        output_attrs = dict(output.attrs)
        self.assertEqual('bob', output.text)
        self.assertTrue(re_search('menu-bob', output_attrs['class']))
        self.assertEqual('/', dict(output.find('a').attrs)['href'])

        output = soup(menu_item(link='/', name='bob', id='bobby', current=True, unavailable=True)).find('li')
        output_attrs = dict(output.attrs)
        self.assertEqual('bob', output.text)
        self.assertTrue(re_search('menu-bobby', output_attrs['class']))
        self.assertTrue(re_search('current', output_attrs['class']))
        self.assertTrue(re_search('unavailable', output_attrs['class']))
        self.assertEqual('/', dict(output.find('a').attrs)['href'])

    def test_calculate_widths(self):
        self.assertEqual([4, 4, 4], calculate_widths(3))
        self.assertEqual([3, 3, 3, 3], calculate_widths(4))
        self.assertEqual([2, 2, 2, 2, 4], calculate_widths(5))
        self.assertEqual([1], calculate_widths(1, 1))

    
