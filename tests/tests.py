"""
Classes to test code.
"""
from django.core.urlresolvers import resolve, reverse
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
        found = resolve(reverse('home'))
        self.assertEqual(found.func, views.word_madness_index)

    def test_root_url_responds(self):
        """
        Test that home page returns 200.
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Word Madness!")
        self.assertContains(response, "Create a new Game")


class CreateGameTest(TestCase):
    """
    Class of tests related to the page for testing games.
    """

    def test_create_game_url_resolves(self):
        """
        Test that game creation page resolves.
        """
        found = resolve(reverse('create'))
        self.assertEqual(found.func, views.create_game)

    def test_create_game_url_get_returns(self):
        """
        Test that game creation get request responds.
        """
        response = self.client.get(reverse('create'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "What Story do you want to tell?")
        self.assertContains(response, "I'm Done")

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
