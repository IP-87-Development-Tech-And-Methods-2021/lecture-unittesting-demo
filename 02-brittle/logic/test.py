import unittest

from urllib.parse import urljoin


class Navigator:
    def __init__(self, base_url):
        self.base_url = base_url
        self.current_url = urljoin(self.base_url, '/')

    def go_to_main_page(self):
        # some other actions
        print('Opening main page')
        self.current_url = urljoin(self.base_url, '/')

    def go_to_albums_page(self):
        # some other actions
        print('Opening albums page')
        self.current_url = urljoin(self.base_url, '/albums')


# =====
# Tests
# =====

class TestNavigator(unittest.TestCase):

    def test_should_navigate_to_albums_page(self):
        base_url = 'https://photos.google.com/'
        nav = Navigator(base_url)

        nav.go_to_albums_page()

        self.assertEqual(nav.current_url, base_url + '/albums')
