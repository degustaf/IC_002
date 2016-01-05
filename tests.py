from django.core.urlresolvers import resolve
from django.test import TestCase
from WordMadness import views

class HomePageTest(TestCase):

    def test_root_url_resolves(self):
        found = resolve('/')
        self.assertEqual(found.func, views.word_madness_index)

class CreateGameTest(TestCase):

    def test_create_game_url_resolves(self):
        found = resolve('/create/')
        self.assertEqual(found.func, views.create_game)

class PlayIndexTest(TestCase):

    def test_play_game_index_resolves(self):
        found = resolve('/play/')
        self.assertEqual(found.func, views.play_index)
