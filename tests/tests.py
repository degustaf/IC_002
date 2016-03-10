"""
Classes to test code.
"""
from django.core.urlresolvers import resolve
from django.test import TestCase
from WordMadness import views


class HomePageTest(TestCase):
    """
    class of tests related to the home page.
    """

    def test_root_url_resolves(self):
        """
        Test that home page resolves.
        """
        found = resolve('/')
        self.assertEqual(found.func, views.word_madness_index)


class CreateGameTest(TestCase):
    """
    Class of tests related to the page for testing games.
    """

    def test_create_game_url_resolves(self):
        """
        Test that game creation page resolves.
        """
        found = resolve('/create/')
        self.assertEqual(found.func, views.create_game)


class PlayIndexTest(TestCase):
    """
    Class of tests related to the index page for playing games.
    """

    def test_play_game_index_resolves(self):
        """
        Test that game index resolves.
        """
        found = resolve('/play/')
        self.assertEqual(found.func, views.play_index)
